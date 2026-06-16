import json
import base64
import re
from io import BytesIO
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image


# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Sustainable E-commerce Route Planning",
    page_icon="🌱",
    layout="wide"
)


# --------------------------------------------------
# Paths
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data" / "outputs"
REPORTS_DIR = BASE_DIR / "reports"
PRESENTATION_DIR = BASE_DIR / "presentation"
NOTEBOOK_PATH = BASE_DIR / "notebooks" / "sustainable_ecommerce_route_planning.ipynb"


# --------------------------------------------------
# Helper functions
# --------------------------------------------------
@st.cache_data
def load_csv(filename):
    path = DATA_DIR / filename

    if not path.exists():
        st.error(f"File not found: {path}")
        return pd.DataFrame()

    return pd.read_csv(path)


def clean_dataframe_for_display(df):
    """
    Hide technical/path-related columns before showing tables in Streamlit.
    """
    if df.empty:
        return df

    hidden_keywords = [
        "path",
        "file_path",
        "filepath",
        "file",
        "source",
        "source_file",
        "url",
        "link",
        "directory",
        "folder",
        "unnamed",
    ]

    cols_to_hide = [
        col for col in df.columns
        if any(keyword in str(col).lower() for keyword in hidden_keywords)
    ]

    return df.drop(columns=cols_to_hide, errors="ignore")


def safe_dataframe(df, message="No data available."):
    if df.empty:
        st.warning(message)
    else:
        display_df = clean_dataframe_for_display(df)
        st.dataframe(display_df, width="stretch", hide_index=True)


def clean_markdown_text(text):
    """
    Hide local file paths inside Markdown or HTML text.
    """
    if not text:
        return text

    text = re.sub(r"/Users/[^\s\)\]\<\"]+", "[local path hidden]", text)
    text = re.sub(r"/mnt/data/[^\s\)\]\<\"]+", "[local path hidden]", text)

    return text


def get_markdown_title(markdown_text):
    """
    Detect Markdown section titles such as:
    # Title
    ## Title
    ### Title
    """
    lines = markdown_text.splitlines()

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("#"):
            title = stripped.lstrip("#").strip()
            if title:
                return title

    return None


def should_skip_notebook_section(title):
    """
    Hide early technical sections from the Streamlit notebook content.
    The notebook itself stays complete; this only controls what appears in the app.
    """
    if not title:
        return True

    title_lower = title.lower().strip()

    # Skip section 1 and 2 of the notebook
    if re.match(r"^(1|2)(\.|\s|$)", title_lower):
        return True

    skip_exact_or_common_titles = [
        "sustainable e-commerce route planning",
        "initial observation",
        "summary interpretation",
        "missing values decision",
        "styled table helper",
        "notebook introduction",
    ]

    if any(skip_title in title_lower for skip_title in skip_exact_or_common_titles):
        return True

    skip_keywords = [
        "download",
        "load",
        "loading",
        "raw",
        "inspect",
        "inspection",
        "cleaning",
        "clean",
        "data preparation",
        "data cleaning",
        "preprocessing",
        "source_file",
        "source file",
        "read data",
        "import data",
        "dataset inspection",
        "helper",
    ]

    if any(keyword in title_lower for keyword in skip_keywords):
        return True

    return False


def is_analytical_notebook_section(title):
    """
    Keep analytical sections only.
    This avoids showing early technical notebook parts in the Streamlit app.
    """
    if not title:
        return False

    title_lower = title.lower().strip()

    # Keep numbered sections from 3 onward
    if re.match(r"^([3-9]|1[0-9])(\.|\s|$)", title_lower):
        return True

    analytical_keywords = [
        "exploratory data analysis",
        "eda",
        "visualization",
        "visualisation",
        "kpi",
        "score",
        "delivery option",
        "decision matrix",
        "top routes",
        "route analysis",
        "co₂",
        "co2",
        "carbon",
        "emission",
        "vehicle",
        "green fleet",
        "traffic context",
        "barcelona traffic",
        "reliability",
        "on-time",
        "validation",
        "spearman",
        "kruskal",
        "outlier",
        "conclusion",
        "future work",
        "limitations",
        "results",
        "analysis",
    ]

    return any(keyword in title_lower for keyword in analytical_keywords)


def is_real_plotly_html(html_data):
    """
    Detect real Plotly outputs and avoid generic Pandas HTML tables.
    Pandas tables may contain local paths such as /Users/...
    """
    html_lower = html_data.lower()

    plotly_signals = [
        "plotly",
        "plotly-graph-div",
        "plotly.js",
        "newplot",
    ]

    return any(signal in html_lower for signal in plotly_signals)


@st.cache_data
def extract_notebook_sections(notebook_path):
    """
    Extract Markdown cells and visual outputs from the notebook.
    Group them by Markdown headings.

    Important:
    - Markdown cells are shown.
    - image/png outputs are shown.
    - Real Plotly HTML charts are shown.
    - Generic HTML tables are NOT shown, because they may expose local file paths.
    """
    sections = []

    if not notebook_path.exists():
        return sections

    with open(notebook_path, "r", encoding="utf-8") as f:
        notebook = json.load(f)

    current_section = {
        "title": "Notebook Introduction",
        "items": []
    }

    visual_counter = 1

    for cell_index, cell in enumerate(notebook.get("cells", []), start=1):
        cell_type = cell.get("cell_type")

        # Markdown cells
        if cell_type == "markdown":
            markdown_text = "".join(cell.get("source", [])).strip()
            markdown_text = clean_markdown_text(markdown_text)

            if not markdown_text:
                continue

            detected_title = get_markdown_title(markdown_text)

            if detected_title:
                if current_section["items"]:
                    sections.append(current_section)

                current_section = {
                    "title": detected_title,
                    "items": []
                }

            current_section["items"].append(
                {
                    "type": "markdown",
                    "cell": cell_index,
                    "content": markdown_text
                }
            )

        # Code cells with visual outputs
        elif cell_type == "code":
            for output in cell.get("outputs", []):
                data = output.get("data", {})

                # Static images: Matplotlib / Seaborn / saved image outputs
                if "image/png" in data:
                    image_data = data["image/png"]

                    if isinstance(image_data, list):
                        image_data = "".join(image_data)

                    try:
                        image_bytes = base64.b64decode(image_data)
                        image = Image.open(BytesIO(image_bytes))

                        current_section["items"].append(
                            {
                                "type": "image",
                                "cell": cell_index,
                                "title": f"Notebook Figure {visual_counter}",
                                "content": image
                            }
                        )

                        visual_counter += 1

                    except Exception:
                        continue

                # HTML outputs: show only real Plotly charts, not Pandas tables
                elif "text/html" in data:
                    html_data = data["text/html"]

                    if isinstance(html_data, list):
                        html_data = "".join(html_data)

                    if is_real_plotly_html(html_data):
                        html_data = clean_markdown_text(html_data)

                        current_section["items"].append(
                            {
                                "type": "html",
                                "cell": cell_index,
                                "title": f"Notebook Interactive Output {visual_counter}",
                                "content": html_data
                            }
                        )

                        visual_counter += 1

    if current_section["items"]:
        sections.append(current_section)

    return sections


# --------------------------------------------------
# Load CSV outputs
# --------------------------------------------------
kpi_df = load_csv("kpi_summary_improved.csv")
score_df = load_csv("delivery_option_score_results.csv")
decision_df = load_csv("route_decision_matrix.csv")
emission_df = load_csv("emission_intensity_by_vehicle.csv")
green_df = load_csv("green_fleet_transition_scenario.csv")
traffic_df = load_csv("barcelona_trams_valid_status_summary.csv")
monthly_traffic_df = load_csv("barcelona_trams_monthly_valid_summary.csv")
distance_df = load_csv("on_time_rate_by_distance_group.csv")
spearman_df = load_csv("statistical_relationship_checks.csv")
category_profile_df = load_csv("score_category_component_profile.csv")
top_routes_df = load_csv("top_delivery_options.csv")
iqr_df = load_csv("iqr_outlier_summary.csv")
co2_vehicle_traffic_df = load_csv("co2_by_vehicle_traffic.csv")
congestion_impact_df = load_csv("congestion_impact_summary.csv")


# --------------------------------------------------
# Styling - dark logistics dashboard theme
# --------------------------------------------------
st.markdown(
    """
    <style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #061421 0%, #0B1F33 45%, #102A43 100%);
        color: #EAF2F8;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1180px;
    }

    /* Main text */
    h1 {
        color: #FFFFFF !important;
        font-weight: 850 !important;
        letter-spacing: -0.03em;
    }

    h2, h3 {
        color: #EAF2F8 !important;
        font-weight: 800 !important;
    }

    p, li {
        color: #EAF2F8 !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #04111D 0%, #0B1F33 100%);
        border-right: 1px solid rgba(46, 204, 113, 0.28);
    }

    section[data-testid="stSidebar"] * {
        color: #EAF2F8 !important;
    }

    div[role="radiogroup"] label {
        color: #EAF2F8 !important;
    }

    /* KPI metric cards */
    div[data-testid="stMetric"] {
        background: #FFFFFF !important;
        border: 1px solid rgba(46, 204, 113, 0.55) !important;
        padding: 1.05rem 1rem !important;
        border-radius: 18px !important;
        box-shadow: 0 14px 34px rgba(0,0,0,0.22) !important;
        min-height: 125px !important;
        overflow: hidden !important;
    }

    /* KPI label */
    div[data-testid="stMetricLabel"],
    div[data-testid="stMetricLabel"] *,
    div[data-testid="stMetric"] label,
    div[data-testid="stMetric"] p {
        color: #52677A !important;
        font-weight: 700 !important;
        opacity: 1 !important;
    }

    /* KPI value */
    div[data-testid="stMetricValue"],
    div[data-testid="stMetricValue"] *,
    div[data-testid="stMetricValue"] div {
        color: #061421 !important;
        font-weight: 900 !important;
        opacity: 1 !important;
        font-size: 2.05rem !important;
        line-height: 1.1 !important;
    }

    /* Project data module cards */
    .section-card {
        background: #FFFFFF !important;
        padding: 1.2rem 1.3rem !important;
        border-radius: 18px !important;
        border: 1px solid rgba(46, 204, 113, 0.55) !important;
        box-shadow: 0 14px 34px rgba(0, 0, 0, 0.22) !important;
        margin-bottom: 1rem !important;
        min-height: 150px !important;
        height: 150px !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: flex-start !important;
        overflow: hidden !important;
    }

    .section-card b {
        color: #061421 !important;
        font-weight: 850 !important;
        font-size: 1rem !important;
        line-height: 1.25 !important;
        margin-bottom: 0.65rem !important;
        display: block !important;
    }

    .section-card span,
    .section-card .small-note {
        color: #425466 !important;
        font-size: 0.92rem !important;
        line-height: 1.55 !important;
    }

    .small-note {
        color: #425466 !important;
    }

    /* Info / alert boxes */
    div[data-testid="stAlert"] {
        background: #EAF7F0 !important;
        border: 1px solid rgba(46, 204, 113, 0.55) !important;
        border-radius: 16px !important;
    }

    div[data-testid="stAlert"] *,
    div[data-testid="stAlert"] p,
    div[data-testid="stAlert"] span,
    div[data-testid="stAlert"] div {
        color: #061421 !important;
        opacity: 1 !important;
        font-weight: 600 !important;
    }

    /* Dataframes */
    div[data-testid="stDataFrame"] {
        background: #FFFFFF !important;
        border-radius: 16px !important;
        overflow: hidden !important;
        border: 1px solid rgba(46, 204, 113, 0.35) !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
    }

    /* Tables */
    table {
        background: #FFFFFF !important;
        color: #061421 !important;
        border-radius: 12px !important;
        overflow: hidden !important;
    }

    th {
        background: #F3F7FA !important;
        color: #061421 !important;
        font-weight: 800 !important;
    }

    td {
        color: #061421 !important;
    }

    /* Plotly chart containers - keep charts inside white cards */
    div[data-testid="stPlotlyChart"] {
        background: #FFFFFF !important;
        border-radius: 18px !important;
        padding: 0.35rem !important;
        border: 1px solid rgba(46, 204, 113, 0.30) !important;
        box-shadow: 0 12px 30px rgba(0,0,0,0.18) !important;
        overflow: hidden !important;
        max-width: 100% !important;
        width: 100% !important;
        box-sizing: border-box !important;
    }

    div[data-testid="stPlotlyChart"] > div,
    div[data-testid="stPlotlyChart"] .js-plotly-plot,
    div[data-testid="stPlotlyChart"] .plotly,
    div[data-testid="stPlotlyChart"] .plot-container,
    div[data-testid="stPlotlyChart"] .svg-container,
    div[data-testid="stPlotlyChart"] svg {
        max-width: 100% !important;
        width: 100% !important;
        box-sizing: border-box !important;
        overflow: hidden !important;
    }

    /* Download buttons */
    .stDownloadButton button {
        background: linear-gradient(90deg, #2ECC71 0%, #00B894 100%) !important;
        color: #061421 !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 800 !important;
        padding: 0.65rem 1rem !important;
    }

    .stDownloadButton button:hover {
        background: linear-gradient(90deg, #3EEB86 0%, #13D9AA 100%) !important;
        color: #061421 !important;
        border: none !important;
    }

    /* Expanders */
    details {
        background: rgba(255, 255, 255, 0.08) !important;
        border: 1px solid rgba(46, 204, 113, 0.25) !important;
        border-radius: 14px !important;
        overflow: hidden !important;
    }

    summary {
        color: #FFFFFF !important;
        font-weight: 750 !important;
    }

    /* Captions */
    .stCaption, caption {
        color: #B8C7D3 !important;
    }

    /* Horizontal rules */
    hr {
        border-color: rgba(46, 204, 113, 0.22) !important;
    }

    /* Code blocks */
    code {
        color: #2ECC71 !important;
        background: rgba(46, 204, 113, 0.10) !important;
        border-radius: 6px !important;
        padding: 0.1rem 0.3rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# Sidebar
# --------------------------------------------------
st.sidebar.title("Dashboard sections")

section = st.sidebar.radio(
    "Choose a section:",
    [
        "Overview",
        "Route Score Explorer",
        "Top Routes",
        "Decision Matrix",
        "Score Components",
        "CO₂ & Vehicles",
        "Green Fleet Scenario",
        "Traffic Context",
        "Reliability",
        "Validation",
        "Notebook Content",
        "Reports & Presentation",
        "Limitations & Future Work",
    ],
)


# --------------------------------------------------
# Overview
# --------------------------------------------------
if section == "Overview":
    st.header("1. Project Overview")

    st.markdown(
        """
        **Main question:**  
        How can delivery route options be compared by balancing time, cost, traffic, reliability and estimated CO₂?

        The datasets were analyzed in modules because they do not share a common transaction ID.
        """
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Avg. route time", "74.25 min")
    col2.metric("Avg. route cost", "565.86 cost units")
    col3.metric("Avg. CO₂", "71.99 kgCO₂e")
    col4.metric("On-time rate", "36.91%")

    st.info(
        "Average optimized route cost represents the typical estimated cost of a route in the dataset. "
        "Since no real currency is specified, the unit is cost units."
    )

    st.subheader("Project data modules")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            """
            <div class="section-card">
            <b>Route planning</b><br>
            <span class="small-note">Time, cost, traffic density, efficiency and reliability.</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            """
            <div class="section-card">
            <b>Carbon footprint</b><br>
            <span class="small-note">Estimated CO₂ by vehicle type, traffic condition and route type.</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            """
            <div class="section-card">
            <b>Tracking reliability</b><br>
            <span class="small-note">On-time and delayed delivery patterns by distance group.</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c4:
        st.markdown(
            """
            <div class="section-card">
            <b>Barcelona TRAMS</b><br>
            <span class="small-note">Real urban traffic context from valid traffic observations.</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.subheader("Main KPI summary")
    safe_dataframe(kpi_df)


# --------------------------------------------------
# Route Score Explorer
# --------------------------------------------------
elif section == "Route Score Explorer":
    st.header("2. Route Score Explorer")

    st.markdown(
        """
        The **Delivery Option Score** is an educational and explainable score.  
        It combines time, cost, estimated CO₂, reliability, traffic and efficiency.

        It is **not** a production routing algorithm.
        """
    )

    if score_df.empty:
        st.warning("Score data is not available.")
    else:
        min_score = float(score_df["delivery_option_score"].min())
        max_score = float(score_df["delivery_option_score"].max())

        score_range = st.slider(
            "Filter routes by Delivery Option Score",
            min_value=round(min_score, 2),
            max_value=round(max_score, 2),
            value=(round(min_score, 2), round(max_score, 2)),
        )

        filtered_score_df = score_df[
            (score_df["delivery_option_score"] >= score_range[0])
            & (score_df["delivery_option_score"] <= score_range[1])
        ]

        fig = px.scatter(
            filtered_score_df,
            x="optimized_route_time_min",
            y="optimized_route_cost",
            color="delivery_option_score",
            size="route_reliability_index",
            hover_data=[
                "route_label",
                "distance_km",
                "estimated_co2_kgco2e",
                "traffic_density_index",
                "score_category",
            ],
            title="Route Time vs Cost with Delivery Option Score",
            labels={
                "optimized_route_time_min": "Optimized route time (min)",
                "optimized_route_cost": "Optimized route cost (cost units)",
                "delivery_option_score": "Delivery Option Score",
                "route_reliability_index": "Reliability index",
            },
            color_continuous_scale="Viridis",
        )

        st.plotly_chart(fig, width="stretch")

        st.subheader("Score distribution")

        fig_hist = px.histogram(
            score_df,
            x="delivery_option_score",
            color="score_category",
            nbins=30,
            title="Distribution of Delivery Option Scores",
            labels={
                "delivery_option_score": "Delivery Option Score",
                "score_category": "Score category",
            },
        )

        st.plotly_chart(fig_hist, width="stretch")

        st.subheader("Filtered route table")
        safe_dataframe(
            filtered_score_df.sort_values("delivery_option_score", ascending=False)
        )


# --------------------------------------------------
# Top Routes
# --------------------------------------------------
elif section == "Top Routes":
    st.header("3. Top Routes")

    st.markdown(
        """
        This section highlights the best route options according to the project-defined educational score.
        """
    )

    if score_df.empty or top_routes_df.empty:
        st.warning("Top route data is not available.")
    else:
        best_route = score_df.sort_values(
            "delivery_option_score", ascending=False
        ).iloc[0]

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.metric("Best route", best_route["route_label"])
        col2.metric("Score", f'{best_route["delivery_option_score"]:.2f}')
        col3.metric("Time", f'{best_route["optimized_route_time_min"]:.2f} min')
        col4.metric("Cost", f'{best_route["optimized_route_cost"]:.2f} cost units')
        col5.metric("CO₂", f'{best_route["estimated_co2_kgco2e"]:.2f} kgCO₂e')

        st.info(
            "Route option 418 is the best route within this educational scoring model. "
            "This does not mean it is a universal real-world optimum."
        )

        top10 = top_routes_df.sort_values("delivery_option_score", ascending=True)

        fig = px.bar(
            top10,
            x="delivery_option_score",
            y="route_label",
            orientation="h",
            title="Top 10 Delivery Options by Score",
            labels={
                "delivery_option_score": "Delivery Option Score",
                "route_label": "Route",
            },
            color="delivery_option_score",
            color_continuous_scale="Viridis",
        )

        st.plotly_chart(fig, width="stretch")

        st.subheader("Top route details")
        safe_dataframe(top_routes_df)


# --------------------------------------------------
# Decision Matrix
# --------------------------------------------------
elif section == "Decision Matrix":
    st.header("4. Decision Matrix")

    st.markdown(
        """
        The decision matrix shows that the best route depends on the decision need:
        speed, cost, reliability or overall balance.
        """
    )

    if decision_df.empty:
        st.warning("Decision matrix data is not available.")
    else:
        fig = px.bar(
            decision_df,
            x="Decision need",
            y="Delivery Option Score",
            color="Decision need",
            title="Delivery Option Score by Decision Need",
            labels={
                "Delivery Option Score": "Delivery Option Score",
                "Decision need": "Decision need",
            },
        )

        st.plotly_chart(fig, width="stretch")

        st.subheader("Decision matrix table")
        safe_dataframe(decision_df)


# --------------------------------------------------
# Score Components
# --------------------------------------------------
elif section == "Score Components":
    st.header("5. Score Component Profile")

    st.markdown(
        """
        This section shows how each score category performs across the six components of the Delivery Option Score.
        """
    )

    if category_profile_df.empty:
        st.warning("Score component profile data is not available.")
    else:
        profile_long = category_profile_df.melt(
            id_vars="score_category",
            value_vars=[
                "time_score",
                "cost_score",
                "co2_score",
                "reliability_score",
                "traffic_score",
                "efficiency_score",
            ],
            var_name="Component",
            value_name="Average score",
        )

        component_labels = {
            "time_score": "Time",
            "cost_score": "Cost",
            "co2_score": "CO₂",
            "reliability_score": "Reliability",
            "traffic_score": "Traffic",
            "efficiency_score": "Efficiency",
        }

        profile_long["Component"] = profile_long["Component"].map(component_labels)

        fig = px.line(
            profile_long,
            x="Component",
            y="Average score",
            color="score_category",
            markers=True,
            title="Average Component Scores by Route Category",
            labels={
                "score_category": "Score category",
                "Average score": "Average component score",
            },
        )

        st.plotly_chart(fig, width="stretch")

        st.subheader("Component profile table")
        safe_dataframe(category_profile_df)


# --------------------------------------------------
# CO2 and Vehicles
# --------------------------------------------------
elif section == "CO₂ & Vehicles":
    st.header("6. CO₂ & Vehicle Analysis")

    st.markdown(
        """
        Emission intensity allows a fairer comparison between vehicle types because it compares emissions per kilometre.
        """
    )

    if emission_df.empty:
        st.warning("Emission intensity data is not available.")
    else:
        emission_sorted = emission_df.sort_values(
            "avg_emission_intensity_kgco2e_per_km",
            ascending=False,
        )

        fig = px.bar(
            emission_sorted,
            x="avg_emission_intensity_kgco2e_per_km",
            y="vehicle_type",
            orientation="h",
            title="Average Emission Intensity by Vehicle Type",
            labels={
                "avg_emission_intensity_kgco2e_per_km": "kgCO₂e per km",
                "vehicle_type": "Vehicle type",
            },
            color="avg_emission_intensity_kgco2e_per_km",
            color_continuous_scale="Viridis",
        )

        fig.update_layout(yaxis={"categoryorder": "total ascending"})
        st.plotly_chart(fig, width="stretch")

        st.subheader("Emission intensity table")
        safe_dataframe(emission_df)

    if not co2_vehicle_traffic_df.empty:
        st.subheader("Average CO₂ by vehicle type and traffic condition")

        expected_traffic_columns = ["Low", "Normal", "High", "Severe Congestion"]
        available_traffic_columns = [
            col for col in expected_traffic_columns
            if col in co2_vehicle_traffic_df.columns
        ]

        if "vehicle_type" in co2_vehicle_traffic_df.columns and available_traffic_columns:
            co2_long = co2_vehicle_traffic_df.melt(
                id_vars="vehicle_type",
                value_vars=available_traffic_columns,
                var_name="Traffic condition",
                value_name="Average CO₂",
            )

            fig2 = px.bar(
                co2_long,
                x="vehicle_type",
                y="Average CO₂",
                color="Traffic condition",
                barmode="group",
                title="Average CO₂ by Vehicle Type and Traffic Condition",
                labels={
                    "vehicle_type": "Vehicle type",
                    "Average CO₂": "Average CO₂ kgCO₂e",
                },
            )

            fig2.update_layout(xaxis_tickangle=-35)
            st.plotly_chart(fig2, width="stretch")

            st.subheader("CO₂ by vehicle and traffic table")
            safe_dataframe(co2_vehicle_traffic_df)


# --------------------------------------------------
# Green Fleet Scenario
# --------------------------------------------------
elif section == "Green Fleet Scenario":
    st.header("7. Green Fleet Transition Scenario")

    if green_df.empty:
        st.warning("Green fleet scenario data is not available.")
    else:
        scenario = green_df.iloc[0]

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Scenario", "50% Diesel → EV")
        col2.metric("Diesel trips", f'{int(scenario["diesel_trips_total"]):,}')
        col3.metric(
            "CO₂ saved",
            f'{scenario["estimated_co2_saved_kgco2e"]:,.0f} kgCO₂e',
        )
        col4.metric("Saving", f'{scenario["estimated_saving_pct"]:.2f}%')

        scenario_chart = pd.DataFrame(
            {
                "Scenario": [
                    "Current diesel emissions",
                    "Estimated EV emissions",
                    "Estimated CO₂ saved",
                ],
                "kgCO₂e": [
                    scenario["current_emissions_for_replaced_trips_kgco2e"],
                    scenario["estimated_ev_emissions_kgco2e"],
                    scenario["estimated_co2_saved_kgco2e"],
                ],
            }
        )

        fig = px.bar(
            scenario_chart,
            x="Scenario",
            y="kgCO₂e",
            title="50% Diesel Van to Electric Van Scenario",
            labels={"kgCO₂e": "kgCO₂e"},
            color="Scenario",
        )

        st.plotly_chart(fig, width="stretch")

        st.info(
            "This is a simplified scenario estimate based on the available dataset, not a full operational fleet simulation."
        )

        safe_dataframe(green_df)


# --------------------------------------------------
# Traffic Context
# --------------------------------------------------
elif section == "Traffic Context":
    st.header("8. Barcelona Traffic Context")

    st.markdown(
        """
        Barcelona TRAMS data is used as real urban traffic context.  
        It is not used as direct route-level input for each delivery route.
        """
    )

    col1, col2 = st.columns(2)

    with col1:
        if traffic_df.empty:
            st.warning("Traffic status data is not available.")
        else:
            fig = px.bar(
                traffic_df,
                x="traffic_status",
                y="share_pct",
                title="Valid Barcelona TRAMS Traffic Status Distribution",
                labels={
                    "traffic_status": "Traffic status",
                    "share_pct": "Share (%)",
                },
                color="traffic_status",
            )

            st.plotly_chart(fig, width="stretch")

    with col2:
        if monthly_traffic_df.empty:
            st.warning("Monthly traffic data is not available.")
        else:
            monthly_df = monthly_traffic_df.copy()
            monthly_df["month"] = monthly_df["month"].astype(str)

            fig_month = px.line(
                monthly_df,
                x="month",
                y="high_congestion_share_of_valid_pct",
                markers=True,
                title="Monthly High Congestion Share",
                labels={
                    "month": "Month",
                    "high_congestion_share_of_valid_pct": "High congestion share (%)",
                },
            )

            st.plotly_chart(fig_month, width="stretch")

    if not congestion_impact_df.empty:
        st.subheader("Congestion impact summary")

        fig_congestion = px.bar(
            congestion_impact_df,
            x="city",
            y="avg_congestion_delay_pct",
            title="Average Congestion Delay by City",
            labels={
                "city": "City",
                "avg_congestion_delay_pct": "Average congestion delay (%)",
            },
            color="city",
        )

        st.plotly_chart(fig_congestion, width="stretch")

    st.subheader("Traffic status table")
    safe_dataframe(traffic_df)

    st.subheader("Monthly traffic table")
    safe_dataframe(monthly_traffic_df)


# --------------------------------------------------
# Reliability
# --------------------------------------------------
elif section == "Reliability":
    st.header("9. Reliability by Distance Group")

    st.markdown(
        """
        Distance alone does not fully explain delivery reliability.  
        In this dataset, shorter routes do not automatically have better on-time performance.
        """
    )

    if distance_df.empty:
        st.warning("Distance reliability data is not available.")
    else:
        fig = px.bar(
            distance_df,
            x="distance_group",
            y="on_time_rate_pct",
            title="On-time Rate by Distance Group",
            labels={
                "distance_group": "Distance group",
                "on_time_rate_pct": "On-time rate (%)",
            },
            color="distance_group",
        )

        st.plotly_chart(fig, width="stretch")

        safe_dataframe(distance_df)


# --------------------------------------------------
# Validation
# --------------------------------------------------
elif section == "Validation":
    st.header("10. Validation Checks")

    st.markdown(
        """
        These checks help verify whether the score behaves logically.
        For example, higher cost, time and estimated CO₂ should generally be associated with lower delivery option scores.
        """
    )

    if spearman_df.empty:
        st.warning("Spearman validation data is not available.")
    else:
        spearman_sorted = spearman_df.sort_values("spearman_rho")

        fig = px.bar(
            spearman_sorted,
            x="spearman_rho",
            y="relationship",
            orientation="h",
            title="Spearman Relationship Checks",
            labels={
                "relationship": "Relationship",
                "spearman_rho": "Spearman rho",
            },
            color="spearman_rho",
            color_continuous_scale="RdBu",
        )

        st.plotly_chart(fig, width="stretch")

        st.subheader("Spearman results")
        safe_dataframe(spearman_df)

    if not iqr_df.empty:
        st.subheader("IQR outlier summary")

        fig_iqr = px.bar(
            iqr_df,
            x="variable",
            y="outlier_share_pct",
            title="Outlier Share by Variable",
            labels={
                "variable": "Variable",
                "outlier_share_pct": "Outlier share (%)",
            },
            color="outlier_share_pct",
            color_continuous_scale="Viridis",
        )

        fig_iqr.update_layout(xaxis_tickangle=-30)
        st.plotly_chart(fig_iqr, width="stretch")

        safe_dataframe(iqr_df)


# --------------------------------------------------
# Notebook Content
# --------------------------------------------------
elif section == "Notebook Content":
    st.header("11. Notebook Content")

    st.markdown(
        """
        This section shows the saved Markdown narrative and visual outputs from the Jupyter Notebook.  
        Only the analytical sections are shown here. Early technical sections related to loading, raw inspection and cleaning are hidden from the Streamlit app.

        For security and cleanliness, generic HTML tables from the notebook are not displayed here, because they may include local file paths.
        """
    )

    notebook_sections = extract_notebook_sections(NOTEBOOK_PATH)

    notebook_sections = [
        section_item for section_item in notebook_sections
        if (
            not should_skip_notebook_section(section_item["title"])
            and is_analytical_notebook_section(section_item["title"])
        )
    ]

    if not notebook_sections:
        st.warning(
            "No saved analytical notebook content was found. "
            "Open the notebook, run all cells, save it, and refresh this Streamlit app."
        )
    else:
        st.success(f"{len(notebook_sections)} analytical notebook sections found.")

        for section_item in notebook_sections:
            with st.expander(section_item["title"], expanded=False):
                for item in section_item["items"]:

                    if item["type"] == "markdown":
                        st.markdown(item["content"])

                    elif item["type"] == "image":
                        st.caption(item["title"])
                        st.image(item["content"], width="stretch")

                    elif item["type"] == "html":
                        st.caption(item["title"])
                        components.html(item["content"], height=650, scrolling=True)

                st.divider()


# --------------------------------------------------
# Reports and Presentation
# --------------------------------------------------
elif section == "Reports & Presentation":
    st.header("12. Reports & Presentation")

    st.markdown(
        """
        This section contains the final written reports and the final presentation PDF.
        Only final PDF files are shown here.
        """
    )

    st.subheader("Reports folder")

    report_files = []
    if REPORTS_DIR.exists():
        report_files = sorted(
            [
                file for file in REPORTS_DIR.glob("*.pdf")
                if not file.name.startswith(".")
            ]
        )

    if report_files:
        for i, file in enumerate(report_files):
            st.write(f"📄 {file.name}")
            with open(file, "rb") as f:
                st.download_button(
                    label=f"Download {file.name}",
                    data=f,
                    file_name=file.name,
                    mime="application/pdf",
                    key=f"report_download_{i}_{file.name}",
                )
    else:
        st.warning("No PDF files found in the reports folder yet.")

    st.subheader("Presentation folder")

    presentation_files = []
    if PRESENTATION_DIR.exists():
        presentation_files = sorted(
            [
                file for file in PRESENTATION_DIR.glob("*.pdf")
                if not file.name.startswith(".")
            ]
        )

    if presentation_files:
        for i, file in enumerate(presentation_files):
            st.write(f"📊 {file.name}")
            with open(file, "rb") as f:
                st.download_button(
                    label=f"Download {file.name}",
                    data=f,
                    file_name=file.name,
                    mime="application/pdf",
                    key=f"presentation_download_{i}_{file.name}",
                )
    else:
        st.warning("No PDF files found in the presentation folder yet.")

# --------------------------------------------------
# Limitations
# --------------------------------------------------
elif section == "Limitations & Future Work":
    st.header("13. Limitations & Future Work")

    st.markdown(
        """
        ### Limitations

        - The datasets come from different sources and were analyzed in modules.
        - There is no common transaction ID across all datasets.
        - The Delivery Option Score uses project-defined weights.
        - The score is educational and explainable, not a production routing algorithm.
        - Barcelona TRAMS is used as urban traffic context, not as direct route-level input.
        - The green fleet scenario is a simplified estimate.
        - Average optimized route cost is expressed in cost units because no real currency is specified.

        ### Future work

        - Add real order and carrier data.
        - Add route-level traffic data.
        - Use Barcelona ITINERARIS travel-time data.
        - Build predictive models for ETA, cost and reliability.
        - Create an interactive decision-support dashboard with adjustable weights.
        """
    )