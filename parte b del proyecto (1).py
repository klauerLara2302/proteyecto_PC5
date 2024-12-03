import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
# Carga el archivo CSV en un DataFrame para realizar análisis de datos.
df = pd.read_csv('juguetes_ventas.csv')
print(df)

# Calcular los ingresos de las ventas
# Crea una nueva columna 'Ingresos', calculando la multiplicación de las columnas 'Ventas' y 'Precio'.
df['Ingresos'] = df['Ventas'] * df['Precio']

# 1. Ventas e ingresos totales por región
# Agrupa los datos por 'Region' y calcula la suma total de las ventas e ingresos por cada región.
ventas_totales_por_region = df.groupby('Region')['Ventas'].sum()
ingresos_totales_por_region = df.groupby('Region')['Ingresos'].sum()
print("Ventas totales por región:\n", ventas_totales_por_region)
print("\nIngresos totales por región:\n", ingresos_totales_por_region)

# 2. Porcentaje de ingresos por región
# Calcula el porcentaje de ingresos de cada región con respecto al total de ingresos.
ingresos_total = ingresos_totales_por_region.sum()
porcentaje_por_cada_region = (ingresos_totales_por_region / ingresos_total) * 100
print("\nPorcentaje de ingresos por región:\n", porcentaje_por_cada_region)

# 3. Ventas por mes
# Convierte la columna 'Fecha' a tipo datetime y extrae el mes para agrupar las ventas por mes.
df['Fecha'] = pd.to_datetime(df['Fecha'])
df['Mes'] = df['Fecha'].dt.to_period('M')
ventas_totales_por_mes = df.groupby('Mes')['Ventas'].sum()
print("\nVentas totales por cada mes:\n", ventas_totales_por_mes)

# 4. Producto más vendido y región más rentable
# Identifica el producto con mayor cantidad de ventas y la región que generó mayores ingresos.
producto_mas_vendido = df.groupby('Producto')['Ventas'].sum().idxmax()
cantidad_vendida_producto = df.groupby('Producto')['Ventas'].sum().max()
region_mas_rentable = df.groupby('Region')['Ingresos'].sum().idxmax()
ingresos_region_mas_rentable = df.groupby('Region')['Ingresos'].sum().max()

# Muestra los resultados del producto más vendido y la región más rentable.
print(f"\nEl producto más vendido es '{producto_mas_vendido}' con un total de {cantidad_vendida_producto} unidades vendidas.")
print(f"La región más rentable es '{region_mas_rentable}' con ingresos totales de {ingresos_region_mas_rentable:.2f} soles.")

# 5. Visualización de las ventas totales por mes
# Genera un gráfico de barras para mostrar las ventas totales agrupadas por mes.
plt.figure(figsize=(10, 5))
ventas_totales_por_mes.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Ventas totales por mes")
plt.xlabel("Mes")
plt.ylabel("Ventas totales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6. Matriz de correlación
# Calcula y muestra la matriz de correlación entre las variables numéricas.
correlacion = df.corr(numeric_only=True)
print("\nMatriz de correlación:\n", correlacion)

# 7. Gráficas adicionales

# a. Ingresos totales por región
# Crea un gráfico de barras para representar los ingresos totales por región.
plt.figure(figsize=(12, 7))
plt.bar(ingresos_totales_por_region.index, ingresos_totales_por_region.values, color='teal', edgecolor='black')
plt.title('Ingresos Totales por Región', fontsize=18, fontweight='bold')
plt.xlabel('Región', fontsize=14)
plt.ylabel('Ingresos (en soles)', fontsize=14)
plt.xticks(rotation=30, ha="right", fontsize='small')
plt.yticks(fontsize="small")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# b. Porcentaje de ventas por producto
# Genera un gráfico circular para visualizar el porcentaje de ventas de cada producto.
ventas_producto = df.groupby('Producto')['Ventas'].sum()
colores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # Colores personalizados
plt.figure(figsize=(8, 8))
plt.pie(ventas_producto, labels=ventas_producto.index, autopct='%1.1f%%', startangle=140, colors=colores)
plt.title('Porcentaje de Ventas por Producto')
plt.show()
# 8. Gráfica de ventas acumuladas por producto

# Calcula las ventas acumuladas por producto y las ordena de mayor a menor.
ventas_acumuladas = df.groupby('Producto')['Ventas'].sum().reset_index()
ventas_acumuladas = ventas_acumuladas.sort_values(by='Ventas', ascending=False)

# Muestra la tabla de ventas acumuladas

print("\nVentas acumuladas por producto:\n", ventas_acumuladas)

# Genera un gráfico de barras para visualizar las ventas acumuladas por producto.
plt.figure(figsize=(7, 7))
plt.bar(ventas_acumuladas['Producto'], ventas_acumuladas['Ventas'], color='skyblue')
plt.title('Ventas Acumuladas por Producto', fontsize=16)
plt.xlabel('Producto', fontsize=14)
plt.ylabel('Ventas Acumuladas', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()