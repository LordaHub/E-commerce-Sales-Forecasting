# 📈 E-commerce Profit Forecasting & Diagnostics

## 📝 Resumen del Proyecto
Este proyecto analiza 3 años de datos de ventas globales (2022-2024) para predecir el rendimiento financiero del primer trimestre de 2025. Se implementó un **modelo híbrido** que combina Regresión Lineal para la tendencia y Descomposición Estacional para ajustar los ciclos mensuales, permitiendo una visión clara del futuro del negocio.

## 📊 Hallazgos Clave (Insights de Negocio)
* **Alerta de Febrero:** El modelo identifica una caída estacional recurrente. Beneficio proyectado: **$43,620**, lo que representa una disminución significativa frente al promedio histórico.
* **Causa Raíz:** Se detectó que la categoría **Office Supplies** actúa como el principal detractor del beneficio durante febrero, rindiendo un 78% menos que el promedio mensual de la categoría.

## 📏 Validación Técnica y Métricas
Para garantizar la fiabilidad del modelo, se realizó una validación cruzada contra los datos históricos (backtesting):
* **MAPE (Mean Absolute Percentage Error):** **11.62%**. Un margen de error altamente competitivo dada la volatilidad natural de la serie.
* **MAE (Error Absoluto Medio):** **$5,956**. Este error representa un ~11% del beneficio promedio mensual ($51,240), validando la robustez del modelo para la toma de decisiones.
* **Análisis de Residuos:** La descomposición muestra residuos aleatorios sin patrones claros, confirmando que los componentes de tendencia y estacionalidad capturan la mayor parte de la señal de los datos.

## 💡 Recomendaciones Estratégicas (Action Plan)
Para mitigar la caída proyectada y optimizar el rendimiento en 2025, se proponen tres acciones concretas:

1. **Pre-emptive Bundling (Enero):** Crear "Kits de Oficina" que agrupen productos de *Office Supplies* con artículos de alta demanda de *Electronics* antes de que inicie la caída de febrero.
2. **Dynamic Stock Reduction:** Reducir las órdenes de compra de suministros de oficina un 20% para el primer trimestre, optimizando el flujo de caja (Cash Flow) y evitando el sobrestock.
3. **Reasignación de Ad-Spend:** Reorientar el 40% del presupuesto publicitario de la categoría *Office* hacia *Accessories* y *Electronics* durante febrero para maximizar el ROAS (Retorno de Inversión Publicitaria).

## 📈 Visualizaciones
### 1. Pronóstico de Beneficios 2025 (Validado)
![Pronóstico 2025](./pronostico_final_2025.png)

### 2. Descomposición de la Serie Temporal
![Descomposición](./descomposicion_serie.png)

## 🛠️ Tecnologías Utilizadas
* **Python 3.13**
* **Pandas & Numpy:** Manipulación de datos y limpieza.
* **Scikit-Learn:** Implementación de la Regresión Lineal.
* **Statsmodels:** Descomposición estacional de series temporales.
* **Matplotlib:** Visualización de datos y dashboards.
