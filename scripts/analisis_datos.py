
# analisis_datos.py
# Script de análisis de ventas - TP Organización Empresarial UTN TUP
# Autor: Paco (P2 - Desarrollador Técnico)

import pandas as pd
import matplotlib.pyplot as plt
import os

# Cargamos el dataset desde la carpeta /datos
# Usamos ruta relativa para garantizar reproducibilidad en Colab
df = pd.read_csv("datos/ventas.csv")

# --- INDICADORES BÁSICOS ---
# Calculamos las ventas totales sumando todas las transacciones
ventas_totales = df["venta_total"].sum()

# Identificamos el producto más vendido por cantidad de unidades
producto_mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()

# Calculamos ventas agrupadas por mes para ver tendencia temporal
ventas_por_mes = df.groupby("mes")["venta_total"].sum()

print(f"Ventas totales: ${ventas_totales}")
print(f"Producto más vendido: {producto_mas_vendido}")
print(f"Ventas por mes:\n{ventas_por_mes}")

# --- GRÁFICO ---
# Gráfico de barras para visualizar evolución mensual de ventas
fig, ax = plt.subplots(figsize=(8, 5))
ventas_por_mes.plot(kind="bar", ax=ax, color="steelblue")
ax.set_title("Evolución de Ventas por Mes")
ax.set_xlabel("Mes")
ax.set_ylabel("Ventas Totales ($)")
plt.tight_layout()

# Guardamos el gráfico en /resultados
os.makedirs("resultados", exist_ok=True)
plt.savefig("resultados/grafico_ventas.png")
print("Gráfico guardado en /resultados")
plt.show()
