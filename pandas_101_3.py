import pandas as pd

inicio = int(input('Introduzca el año inicial: '))
fin = int(input('Introduzca el año final: '))

ventas = {}  # Inicializar el diccionario de ventas

# Solicitar las ventas para cada año en el rango especificado
for i in range(inicio, fin + 1):
    ventas[i] = float(input('Introduzca las ventas del año ' + str(i) + ': '))

# Crear una Serie de pandas con los datos de ventas
serie_ventas = pd.Series(ventas)

# Mostrar las ventas originales
print('Ventas:\n', serie_ventas)

# Aplicar un descuento del 10% y mostrar las ventas con descuento
ventas_descuento = serie_ventas * 0.9
print('Ventas con descuento del 10%:\n', ventas_descuento)
