# Planificación Sostenible de Rutas para E-commerce

## Análisis basado en datos de tiempo, tráfico, coste y CO₂

Este repositorio contiene un proyecto final de Data Analytics centrado en logística sostenible para e-commerce y toma de decisiones en entregas de última milla.

La idea principal del proyecto es simple: una opción de entrega no debería evaluarse solo por rapidez o coste. Una mejor decisión logística debe equilibrar rendimiento operativo e impacto ambiental, incluyendo tiempo de entrega, coste de ruta, condiciones de tráfico, fiabilidad, eficiencia y emisiones estimadas de CO₂.

> Este es un proyecto educativo de análisis de datos. El modelo de puntuación es intencionadamente simple, transparente y explicable. No es un algoritmo de enrutamiento en producción.

---

## Dashboard interactivo

El dashboard interactivo en Streamlit está disponible aquí:

https://sustainable-ecommerce-route-planning.streamlit.app/

El dashboard presenta los principales resultados del proyecto final del Sprint 13, incluyendo la puntuación de rutas, las mejores opciones de entrega, el análisis de CO₂ y vehículos, el contexto de tráfico, los indicadores de fiabilidad, las comprobaciones de validación, los informes, la presentación y las salidas del notebook.

---

## Objetivos del proyecto

- Analizar el rendimiento de rutas de entrega de e-commerce.
- Estudiar la relación entre tiempo, distancia, coste, tráfico y fiabilidad.
- Analizar emisiones de CO₂ por tipo de vehículo, tipo de ruta y condición de tráfico.
- Añadir contexto urbano real usando datos abiertos de tráfico de Barcelona.
- Construir un **Delivery Option Score** simple y explicable.
- Generar outputs CSV, una presentación final y un informe del proyecto.

---

## Estructura del repositorio

```text
sustainable-ecommerce-route-planning/
│
├── README.md
├── README_ES.md
├── requirements.txt
├── app.py
│
├── notebooks/
│   └── sustainable_ecommerce_route_planning.ipynb
│
├── data/
│   ├── raw/
│   └── outputs/
│
├── presentation/
│   └── sustainable_ecommerce_route_planning_presentation_EN_final.pdf
│
└── reports/
    ├── report_Sprint_13_Sustainable_Ecommerce_Route_planning.pdf
    └── informe_Sprint_13_Sustainable_Ecommerce_Route_planning.pdf
```

La presentación final se incluye en PDF. La versión editable de PowerPoint se mantiene por separado para evitar aumentar el tamaño del repositorio.

---

## Datasets utilizados

El proyecto combina cuatro fuentes de datos públicas o simuladas:

1. **E-commerce Logistics Route Planning Dataset**  
   Dataset principal de rutas, tiempo, coste, tráfico, eficiencia y fiabilidad.

2. **Green Logistics Carbon Footprint Dataset**  
   Dataset de emisiones de CO₂, tipo de vehículo, tipo de ruta y tráfico.

3. **Transportation and Logistics Tracking Dataset**  
   Fuente de apoyo para analizar puntualidad, retrasos, congestión y fiabilidad.

4. **Barcelona TRAMS Traffic Dataset**  
   Datos abiertos de tráfico de Barcelona usados como contexto urbano real.

---

## Metodología

El análisis sigue un flujo sencillo y reproducible:

1. Carga de datos.
2. Limpieza y preparación.
3. Análisis exploratorio de datos.
4. Cálculo de KPIs.
5. Construcción del Delivery Option Score.
6. Validación visual y estadística.
7. Exportación de outputs finales.
8. Presentación de conclusiones, limitaciones y trabajo futuro.

El análisis es modular porque los datasets no comparten un identificador común de transacción.

---

## Delivery Option Score

El **Delivery Option Score** compara opciones de ruta usando una lógica simplificada de análisis multicriterio.

Componentes usados:

| Componente | Peso | Dirección |
|---|---:|---|
| Tiempo | 20% | Menor es mejor |
| Coste | 20% | Menor es mejor |
| CO₂ estimado | 25% | Menor es mejor |
| Fiabilidad | 20% | Mayor es mejor |
| Tráfico | 10% | Menor es mejor |
| Eficiencia | 5% | Mayor es mejor |

La mejor opción global encontrada fue:

| Ruta | Score | Tiempo | Coste | CO₂ estimado | Fiabilidad |
|---|---:|---:|---:|---:|---:|
| Route option 418 | 92.62 | 15.33 min | 85.07 unidades de coste | 2.04 kgCO₂e | 0.863 |

---

## Principales resultados

- La ruta más rápida o más barata no siempre es la mejor opción global.
- Las emisiones de CO₂ varían mucho según el tipo de vehículo.
- El tráfico afecta tanto al rendimiento operativo como a la sostenibilidad.
- La fiabilidad es clave para conectar logística y experiencia del cliente.
- El contexto urbano de Barcelona ayuda a interpretar la fricción real de la ciudad.
- Un score transparente puede ayudar a comparar trade-offs de forma explicable.

---

## Limitaciones

- Los datasets son públicos o simulados.
- No existe un ID común para unir todas las fuentes fila por fila.
- El score usa pesos educativos definidos para este proyecto.
- No se incluyen precios reales de operadores, rutas reales de reparto ni datos en tiempo real.
- Barcelona TRAMS se usa como contexto urbano, no como input directo de rutas reales.
- El modelo no es un sistema de producción.

---

## Trabajo futuro

- Integrar datos de tráfico en tiempo real.
- Añadir APIs de carriers y datos reales de entregas.
- Construir modelos predictivos para ETA, coste, CO₂ o fiabilidad.
- Crear un dashboard interactivo con pesos ajustables.
- Mejorar la estimación de CO₂ con datos más detallados de vehículo, carga y combustible.

---

## Conclusión

Este proyecto muestra cómo diferentes fuentes de datos de logística, sostenibilidad y tráfico pueden combinarse para apoyar decisiones de entrega más transparentes.

El resultado principal es un marco educativo y explicable para comparar opciones de entrega equilibrando tiempo, coste, tráfico, fiabilidad y emisiones estimadas de CO₂.
