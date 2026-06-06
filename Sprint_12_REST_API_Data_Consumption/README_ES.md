# Sprint 12 - Consumo de datos desde una API REST

Este proyecto forma parte del Sprint 12 del itinerario de Data Analytics.  
El objetivo principal es practicar el consumo de datos desde APIs REST utilizando Python, interpretar códigos de estado HTTP, trabajar con respuestas en formato JSON y transformar los datos obtenidos en DataFrames de pandas.

El ejercicio está desarrollado en un Jupyter Notebook y se organiza en tres niveles.

---

## Objetivos del proyecto

En este sprint se trabajan los siguientes puntos:

- Realizar peticiones HTTP con la librería `requests`.
- Consultar APIs públicas mediante el método `GET`.
- Interpretar códigos de estado como `200`, `201` y `404`.
- Enviar peticiones `POST`, `PATCH` y `DELETE`.
- Leer respuestas en formato JSON.
- Transformar datos JSON en DataFrames de pandas.
- Consultar datasets públicos mediante la API de Open Data Barcelona.
- Exportar los datos finales a un archivo `.csv`.

---

## Tecnologías utilizadas

- Python
- Jupyter Notebook
- requests
- pandas
- json
- APIs REST
- Open Data Barcelona API

---

## Estructura del notebook

### Nivel 1 - Exploración básica con JSONPlaceholder

En el primer nivel se utiliza la API pública JSONPlaceholder para practicar diferentes métodos HTTP.

Se realizan las siguientes operaciones:

- Consulta de recursos con `GET`:
  - `/posts`
  - `/users`
  - `/todos`
- Revisión del código de estado y de la cantidad total de registros.
- Consulta de una publicación inexistente para obtener un error `404`.
- Creación ficticia de una publicación mediante `POST`.
- Modificación parcial de una publicación mediante `PATCH`.
- Eliminación ficticia de una publicación mediante `DELETE`.

JSONPlaceholder se utiliza como API de práctica, por lo que las operaciones de creación, modificación y eliminación devuelven una respuesta, pero no modifican realmente los datos del servidor.

---

### Nivel 2 - Interacción con una API pública real

En el segundo nivel se trabaja con REST Countries API, una API pública seleccionada desde el repositorio Public APIs.

Antes de seleccionar esta API, se revisaron opciones más relacionadas con sostenibilidad y huella de carbono, como CO2 Offset. Sin embargo, para este ejercicio se eligió REST Countries API porque ofrece endpoints claros, no requiere autenticación, devuelve datos en formato JSON y permite transformar fácilmente la respuesta en un DataFrame.

En este nivel se realiza:

- Revisión de endpoints disponibles.
- Revisión de parámetros útiles, como `fields`.
- Petición `GET` al endpoint `/v3.1/region/europe`.
- Extracción de campos como país, capital, región, población, idiomas y monedas.
- Conversión de la respuesta JSON en un DataFrame de pandas.

Durante la transformación se preparan algunos campos anidados, como `name`, `capital`, `languages` y `currencies`, para obtener una tabla más clara y fácil de analizar.

---

### Nivel 3 - API de Open Data Barcelona

En el tercer nivel se utiliza la API de Open Data Barcelona para buscar y consultar datos públicos de la ciudad.

La búsqueda se centra en temas relacionados con Kamport y con el proyecto final de Data Analytics: logística urbana, última milla, zonas de carga y descarga, tráfico, restricciones urbanas, calidad del aire y sostenibilidad.

Para encontrar un dataset adecuado se utiliza `package_search` con diferentes palabras clave. Finalmente se selecciona el dataset:

`zones-carrega-descarrega`

Este dataset contiene información sobre las zonas de carga y descarga de la ciudad de Barcelona. No contiene datos directos de entregas o paquetes, pero sí información sobre una infraestructura urbana relacionada con la logística de última milla.

Después se utiliza:

- `package_show` para revisar los detalles del dataset.
- Selección de un recurso en formato CSV con `datastore_active = True`.
- `datastore_search` para recuperar 100 registros.
- Conversión de los registros en un DataFrame.
- Exportación del DataFrame a un archivo CSV.

El archivo generado es:

`zonas_carga_descarga_barcelona.csv`

---

## Archivo generado

El notebook genera un archivo CSV con los registros recuperados desde Open Data Barcelona:

`zonas_carga_descarga_barcelona.csv`

Este archivo puede reutilizarse en análisis posteriores o en otras herramientas de análisis de datos.

---

## Relación con Kamport

Kamport es un proyecto orientado a la logística urbana y la última milla.

Aunque este sprint es principalmente una práctica técnica sobre APIs REST, el dataset elegido en el Nivel 3 tiene relación con el contexto urbano de Kamport. Las zonas de carga y descarga pueden ser relevantes para entender dónde existen espacios habilitados para operaciones de reparto, carga y descarga dentro de la ciudad de Barcelona.

Este tipo de datos podría ser útil en análisis futuros relacionados con:

- Planificación de rutas urbanas.
- Identificación de zonas logísticas dentro de la ciudad.
- Optimización de operaciones de última milla.
- Análisis de infraestructura urbana para reparto.
- Sostenibilidad y movilidad urbana.

---

## Conclusión

Este sprint me ha permitido practicar el consumo de datos desde APIs REST de forma progresiva.

Primero he trabajado con una API de laboratorio para entender los métodos HTTP principales. Después he consultado una API pública real y he transformado su respuesta JSON en un DataFrame. Finalmente, he utilizado la API de Open Data Barcelona para buscar un dataset, seleccionar un recurso adecuado, recuperar registros reales y exportarlos a un archivo CSV.

Este flujo es importante para el trabajo de un Data Analyst, ya que muchas fuentes de datos reales se consultan mediante APIs y requieren transformar respuestas JSON en estructuras tabulares para poder analizarlas.
