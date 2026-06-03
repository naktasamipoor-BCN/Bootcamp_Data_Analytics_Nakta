# Sprint 11 - Visualización de Datos con Python y Power BI

Este repositorio contiene la entrega de la Tasca S11.01, centrada en la visualización de datos con Python y su integración con Power BI.

## Objetivo

El objetivo de esta práctica es trabajar el proceso completo de visualización de datos: conexión con MySQL, carga y preparación de datos en Python, creación de visualizaciones con Pandas, Matplotlib y Seaborn, y traslado de las visualizaciones principales a Power BI mediante scripts de Python.

## Base de datos utilizada

La práctica utiliza la base de datos `sprint4_star`, creada en el Sprint 4.

A partir de las tablas del modelo en estrella se crea un DataFrame principal llamado `df_analysis`, que combina información de transacciones, productos, empresas, usuarios, estado de tarjeta y datos temporales y geográficos.

## Carga de datos en Power BI

Para mantener la coherencia entre el notebook y el informe de Power BI, en Power BI no se cargan todas las tablas de la base de datos por separado.

En su lugar, se utiliza una consulta SQL que genera la misma estructura de datos utilizada en Python para crear `df_analysis`. De esta forma, el informe de Power BI trabaja con un único conjunto de datos preparado para el análisis y evita cargar tablas innecesarias.

La columna `row_id` se mantiene como identificador único de cada registro, ya que una misma transacción puede contener varios productos. Esto ayuda a evitar problemas de duplicados o pérdida de información en Power BI.

## Archivos incluidos

- `sprint11 Final.ipynb`: notebook de Jupyter ejecutado con las soluciones, visualizaciones e interpretaciones.
- `sprint11 Final.pbix`: informe de Power BI con las visualizaciones del Nivel 1 trasladadas mediante scripts de Python.
- `sprint11 Final.pdf`: versión exportada del informe de Power BI para visualizar el resultado final sin abrir Power BI.
- `requirements.txt`: librerías necesarias para ejecutar el notebook.
- `.gitignore`: archivo para evitar subir carpetas o archivos innecesarios.
- `README.md`: descripción general del proyecto y de la estructura de la entrega.

## Herramientas utilizadas

- Python
- Jupyter Notebook
- Pandas
- Matplotlib
- Seaborn
- SQLAlchemy
- MySQL
- Power BI

## Estructura del análisis

El notebook se organiza en tres niveles:

### Nivel 1

Creación de visualizaciones básicas según el tipo de variables:

- Una variable numérica
- Dos variables numéricas
- Una variable categórica
- Una variable categórica y una numérica
- Dos variables categóricas
- Tres variables combinadas
- Pairplot

También se incluye un boxplot adicional como análisis complementario.

### Nivel 2

Análisis de correlación entre variables numéricas y creación de un jointplot para explorar la relación entre `weight` y `price`.

### Nivel 3

Traslado de las visualizaciones del Nivel 1 a Power BI utilizando objetos visuales de Python.

## Nota sobre los scripts en Power BI

En Power BI, los scripts de Python utilizan el DataFrame automático `dataset`, que contiene las columnas añadidas al objeto visual.

Por este motivo, los scripts son equivalentes a los utilizados en el notebook, pero sustituyendo `df_analysis` por `dataset`.

## Entrega

La entrega final incluye el notebook ejecutado y el archivo `.pbix` dentro de esta carpeta del repositorio.