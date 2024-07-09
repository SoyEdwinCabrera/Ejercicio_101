import pandas as pd

# Crear un marco de datos
df = pd.DataFrame({'a': [1, 2, 3, 4], 'b': [5, 6, 7, 8], 'c': [9, 10, 11, 12]})

# Seleccionar las columnas 'a' y 'b'
df_columns = df[['a', 'b']]

# Filtrar el DataFrame para incluir solo filas donde el valor en la columna 'a' sea mayor a 2
df_filtrado = df[df['a'] > 2]

print("DataFrame con columnas 'a' y 'b':")
print(df_columns)

print("\nDataFrame filtrado (columna 'a' > 2):")
print(df_filtrado)
