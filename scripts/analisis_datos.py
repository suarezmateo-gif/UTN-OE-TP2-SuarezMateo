# analisis_datos.py
# Script de análisis de ventas - TP Organización Empresarial UTN TUP
# Revisado por: Luis (P3 - Revisor y QA)

import pandas as pd
import matplotlib.pyplot as plt
import os

# CARGA DE DATOS
# Ruta relativa para garantizar reproducibilidad en cualquier entorno
df = pd.read_csv("datos/ventas.csv")

# Verificamos que el dataset cargó correctamente antes de procesar
print(f"Dataset cargado: {df.shape[0]} registros, {df.shape[1]} columnas")

# INDICADORES
# Suma total de todas las ventas del período
ventas_totales = df["venta_total"].sum()

# El producto más vendido se mide por unidades, no por monto
# para reflejar popularidad y no solo rentabilidad
producto_mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()

# Agrupamos por mes para detectar tendencias temporales
ventas_por_mes = df.groupby("mes")["venta_total"].sum()

print(f"Ventas totales del período: ${ventas_totales:,.2f}")
print(f"Producto más vendido: {producto_mas_vendido}")
print(f"Ventas por mes:\n{ventas_por_mes}")

# VISUALIZACIÓN
# Gráfico de barras para comparar desempeño mensual visualmente
fig, ax = plt.subplots(figsize=(8, 5))
ventas_por_mes.plot(kind="bar", ax=ax, color="steelblue", edgecolor="black")
ax.set_title("Evolución de Ventas por Mes", fontsize=14)
ax.set_xlabel("Mes", fontsize=12)
ax.set_ylabel("Ventas Totales ($)", fontsize=12)
ax.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

os.makedirs("resultados", exist_ok=True)
# DPI 150 para mejor calidad de imagen exportada
plt.savefig("resultados/grafico_ventas.png", dpi=150)
print("Gráfico guardado correctamente en /resultados")
plt.show()
