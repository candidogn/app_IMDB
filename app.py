import pandas as pd

# Cargar el dataset
data = pd.read_csv('/ruta/del/archivo.csv')

# Ordenar las películas por ingresos de mayor a menor y seleccionar las 10 primeras
top_10_revenue = data.sort_values(by='Revenue (Millions)', ascending=False).head(10)

# Mostrar el título y los ingresos de estas 10 películas
print(top_10_revenue[['Title', 'Revenue (Millions)']])
