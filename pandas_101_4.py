import pandas as pd

def estadisticas_notas(notas):
    notas = pd.Series(notas)
    estadisticos = pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()],
                             index=['Min', 'Max', 'Media', 'Desviación típica'])
    return estadisticos

notas = {'Juan': 9, 'María': 6.5, 'Pedro': 4, 'Carmen': 8.5, 'Luis': 5}
print(estadisticas_notas(notas))

