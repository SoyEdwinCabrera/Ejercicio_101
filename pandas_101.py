import pandas as pd

# Crear un marco de datos
df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})

# Seleccionar las dos primeras filas del DataFrame
df_primeras_dos_filas = df.head(2)

# Seleccionar las columnas 'a' y 'b' del DataFrame
df_ab_columns = df[['a', 'b']]

# Filtrar el DataFrame para incluir solo filas donde la columna 'a' sea mayor que 5
df_filtrado = df[df['a'] > 5]

# Calcular la media de las columnas 'a' y 'b' para cada grupo de datos mediante la columna 'c'
df_grouped_mean = df.groupby('c').mean()

# Crear una nueva columna llamada 'd' que sea la suma de las columnas 'a' y 'b'
df['d'] = df['a'] + df['b']

# Reemplazar todos los valores en la columna 'c' que sean mayores que 8 con el valor 10
df['c'] = df['c'].replace({9: 10})

print("DataFrame completo:")
print(df)
print("\nLas dos primeras filas:")
print(df_primeras_dos_filas)
print("\nColumnas 'a' y 'b':")
print(df_ab_columns)
print("\nFiltrado (columna 'a' > 5):")
print(df_filtrado)
print("\nMedia de las columnas agrupadas por 'c':")
print(df_grouped_mean)
