import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.linear_model import LinearRegression

# ==========================================
# 1. CARGA Y LIMPIEZA DE DATOS
# ==========================================
df = pd.read_csv('ecommerce_sales_data.csv')
df['Order Date'] = pd.to_datetime(df['Order Date'])

print(f"Rango de datos: {df['Order Date'].min()} a {df['Order Date'].max()}")

# Agregación mensual
resumen_financiero = df.resample('ME', on='Order Date').agg({
    'Sales': 'sum',
    'Profit': 'sum'
})

# Métrica de eficiencia
resumen_financiero['Profit_Margin_%'] = (resumen_financiero['Profit'] / resumen_financiero['Sales']) * 100

# ==========================================
# 2. ANÁLISIS ESTADÍSTICO Y DESCOMPOSICIÓN
# ==========================================
print("\n--- Volatilidad del Beneficio ---")
print(resumen_financiero['Profit'].describe())

# Descomposición de la serie temporal
descomposicion = seasonal_decompose(resumen_financiero['Profit'], model='additive')

# Guardar gráfico de descomposición
fig_desc = descomposicion.plot()
fig_desc.set_size_inches(12, 8)
plt.savefig('descomposicion_serie.png', dpi=300, bbox_inches='tight')
plt.show()

# ==========================================
# 3. MODELO PREDICTIVO (REGRESIÓN + ESTACIONALIDAD)
# ==========================================
# Preparar datos para Regresión Lineal
resumen_financiero['Mes_Num'] = np.arange(len(resumen_financiero))
X = resumen_financiero[['Mes_Num']]
y = resumen_financiero['Profit']

modelo = LinearRegression()
modelo.fit(X, y)

# Predicción lineal simple para los meses 36, 37 y 38 (Ene, Feb, Mar 2025)
futuro_idx = np.array([[36], [37], [38]])
pred_lineal = modelo.predict(futuro_idx)

# Ajuste por Estacionalidad (Nivel Experto)
estacionalidad_media = descomposicion.seasonal.groupby(descomposicion.seasonal.index.month).mean()
ene_ajustado = pred_lineal[0] + estacionalidad_media[1]
feb_ajustado = pred_lineal[1] + estacionalidad_media[2]
mar_ajustado = pred_lineal[2] + estacionalidad_media[3]

print("\n--- PREDICCIÓN AJUSTADA 2025 ---")
print(f"Enero: ${ene_ajustado:.2f} | Febrero: ${feb_ajustado:.2f} | Marzo: ${mar_ajustado:.2f}")

# ==========================================
# 4. VISUALIZACIÓN FINAL Y PORTFOLIO
# ==========================================
fechas_futuras = pd.date_range(start='2025-01-01', periods=3, freq='ME')
df_prediccion = pd.DataFrame({'Profit': [ene_ajustado, feb_ajustado, mar_ajustado]}, index=fechas_futuras)

plt.figure(figsize=(14, 7))
plt.plot(resumen_financiero.index, resumen_financiero['Profit'], label='Histórico Real', color='blue', marker='o')

# Conectar el último punto real con la predicción
ultimo_punto_real = resumen_financiero.iloc[[-1]][['Profit']]
df_final_plot = pd.concat([ultimo_punto_real, df_prediccion])

plt.plot(df_final_plot.index, df_final_plot['Profit'], label='Predicción Ajustada', color='red', linestyle='--', marker='s')
plt.axvline(x=resumen_financiero.index[-1], color='gray', linestyle=':', alpha=0.5)
plt.title('Pronóstico de Beneficios 2025: Análisis de Tendencia + Estacionalidad', fontsize=16)
plt.legend()
plt.grid(True, alpha=0.3)

plt.savefig('pronostico_final_2025.png', dpi=300, bbox_inches='tight')
plt.show()

# ==========================================
# 5. DIAGNÓSTICO POR CATEGORÍA (FEBRERO)
# ==========================================
df_febreros = df[df['Order Date'].dt.month == 2]
analisis_categoria = df_febreros.groupby('Category')['Profit'].sum().sort_values()

plt.figure(figsize=(10, 6))
analisis_categoria.plot(kind='barh', color='salmon')
plt.title('Diagnóstico de Febrero: Beneficios por Categoría', fontsize=14)
plt.xlabel('Beneficio Acumulado ($)')
plt.grid(axis='x', linestyle='--', alpha=0.6)

plt.savefig('diagnostico_categorias_febrero.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n✅ Proceso completado. Gráficos guardados en la carpeta del proyecto.")