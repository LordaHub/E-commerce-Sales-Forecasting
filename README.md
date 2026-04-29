# 📈 E-commerce Profit Forecasting & Diagnostics

## Resumen del Proyecto
Este proyecto analiza 3 años de datos de ventas de un e-commerce para predecir el rendimiento financiero del primer trimestre de 2025. Utilicé un modelo híbrido que combina **Regresión Lineal** con **Ajustes Estacionales** para obtener pronósticos precisos.

## Key Insights (Hallazgos Clave)
* **Tendencia:** El negocio muestra un crecimiento sostenido desde 2022, aunque con una ligera desaceleración al cierre de 2024.
* **Alerta de Febrero:** Se identificó una caída estacional recurrente en febrero. El modelo predice un beneficio de **$43,028**, significativamente menor al promedio mensual de $51k.
* **Causa Raíz:** El diagnóstico por categoría reveló que **Office Supplies** tiene un rendimiento 78% inferior al resto de las categorías durante febrero.

## Tecnologías Utilizadas
* **Python** (Pandas, Numpy)
* **Análisis Estadístico:** Statsmodels (Seasonal Decompose)
* **Machine Learning:** Scikit-Learn (Linear Regression)
* **Visualización:** Matplotlib

## Visualizaciones

### 1. Pronóstico 2025
![Pronóstico 2025](./pronostico_final_2025.png)
*Gráfico comparativo entre datos históricos y predicción ajustada.*

### 2. Diagnóstico de Categorías
![Diagnóstico Febrero](./diagnostico_categorias_febrero.png)
*Análisis de por qué cae el beneficio en febrero.*

### 3. Descomposición de la Serie
![Descomposición](./descomposicion_serie.png)
*Análisis de tendencia y estacionalidad.*
