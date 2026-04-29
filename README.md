# 📈 E-commerce Profit Forecasting & Diagnostics

## 📝 Resumen del Proyecto
Este proyecto analiza 3 años de datos de ventas globales (2022-2024) para predecir el rendimiento financiero del primer trimestre de 2025. Se implementó un **modelo híbrido** que combina Regresión Lineal (tendencia) con Descomposición Estacional.

## 📊 Hallazgos Clave (Insights)
* **Alerta de Febrero:** El modelo predice una caída estacional recurrente. Beneficio proyectado: **$43,620**, un 15% por debajo del promedio.
* **Causa Raíz:** Se identificó que la categoría **Office Supplies** rinde un 78% menos que el promedio durante febrero, siendo el principal detractor del beneficio.

## 📏 Rendimiento y Validación
Para garantizar la fiabilidad, se validó el modelo contra los datos históricos:
* **MAE (Error Absoluto Medio):** $5,956.
* **Error Porcentual:** 11.62%.
* **Precisión Final:** **88.38%**.
* **Impacto:** El ajuste estacional mejoró la precisión del pronóstico en un 22% frente a una regresión lineal simple.

## 💡 Recomendaciones Estratégicas
1. **Liquidación Proactiva:** Ofertas de "Back to Office" a finales de enero para mitigar la caída de febrero en suministros de oficina.
2. **Reasignación de Marketing:** Priorizar categorías de *Accessories* y *Electronics* durante febrero, ya que mantienen márgenes estables.

## 📈 Visualizaciones
### 1. Pronóstico de Beneficios 2025
![Pronóstico 2025](./pronostico_final_2025.png)

### 2. Descomposición de la Serie Temporal
![Descomposición](./descomposicion_serie.png)
