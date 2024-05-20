# -*- coding: utf-8 -*-
"""
Created on Fri May 17 16:53:45 2024
@author: GustavoGutierrez
"""

import csv

"""
---------------------
CARGA DEL ARCHIVO CSV
---------------------
"""


# Función para leer datos del archivo CSV
def leer_datos(file_name):
    with open(file_name, mode='r') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        data = [row for row in csv_reader]
    return data
# Especifica la ruta de tu archivo CSV
file_name = 'D:\\INFORMATICA\\1 - 2024\\INF 354\\sunpots.csv'


# Leer los datos
dataset = leer_datos(file_name)

# Imprimir los datos para verificar
#for row in dataset:
 #   print(row)


"""
---------------------
INCISO A)
---------------------
"""
print('------------------------')
print('INCISO A)')
print('------------------------')


# Función para calcular percentiles
def calcular_percentil(data, percentil):
    size = len(data)
    pos = (size + 1) * percentil / 100.0
    pos_int = int(pos)
    pos_frac = pos - pos_int
    
    if pos_int == 0:
        return data[0]
    if pos_int >= size:
        return data[-1]
    
    valor_inf = data[pos_int - 1]
    valor_sup = data[pos_int]
    
    return valor_inf + pos_frac * (valor_sup - valor_inf)

# Función para calcular el cuartil 75 y el percentil 80
def calcular_cuartil_75_y_percentil_80(dataset):
    resultados = {}
    for columna in dataset[0].keys():
        # Extraer los datos de la columna y convertir a flotantes
        try:
            datos_columna = sorted([float(fila[columna]) for fila in dataset])
        except ValueError as e:
            print(f"Error al convertir los datos de la columna {columna}: {e}")
            continue
        
        # Calcular el cuartil 75 y el percentil 80
        cuartil_75 = calcular_percentil(datos_columna, 75)
        percentil_80 = calcular_percentil(datos_columna, 80)
        
        resultados[columna] = {
            'cuartil_75': cuartil_75,
            'percentil_80': percentil_80
        }
        
    return resultados

# Calcular resultados
resultados = calcular_cuartil_75_y_percentil_80(dataset)

# Imprimir resultados
for columna, valores in resultados.items():
    print(f"Columna: {columna}")
    print(f"Cuartil 75: {valores['cuartil_75']}")
    print(f"Percentil 80: {valores['percentil_80']}\n")
    
print("CUARTIL: Para la primera columna Y (Año) significa el año donde el 75% de los datos estan por debajo del año 1971")
print("PERCENTIL 80: Para la primera columna Y (Año) significa el año donde el 80% de los datos estan por debajo del año 1981")    

print("CUARTIL: Para la segunda columna M (Mes) significa el mes donde el 75% de los datos estan por debajo del mes 10 osea octubre")
print("PERCENTIL 80: Para la segunda columna M (Mes) significa el mes donde el 80% de los datos estan por debajo del mes 10 osea octubre")

print("CUARTIL: Para la tercer columna D (Dia) significa el dia donde el 75% de los datos estan por debajo del dia 23")
print("PERCENTIL 80: Para la tercer columna D (Dia) significa el dia donde el 80% de los datos estan por debajo del dia 25")

print("CUARTIL: Para la cuarta columna DTS (Numero total de manchas solares por dia) el 75% de los datos estan por debajo de 123")
print("PERCENTIL 80: Para la cuarta columna D (Numero total de manchas solares por dia) el 80% de los datos estan por debajo de 142")

print("CUARTIL: Para la quinta columna DE (Desviacion estandar) el 75% de los datos estan por debajo de 10")
print("PERCENTIL 80: Para la quinta columna DE (desviacion estandar) el 80% de los datos estan por debajo de 10.9")

print("CUARTIL: Para la sexta columna #OBS (Observaciones por dia) el 75% de los datos estan por debajo de 1")
print("PERCENTIL 80: Para la sexta columna #OBS (Observaciones por dia) el 80% de los datos estan por debajo de 7")

print("CUARTIL: Para la septima columna IN (Indicador provisional) el 75% de los datos estan por debajo de 1")
print("PERCENTIL 80: Para la septima columna IN (Indicador provisional) el 80% de los datos estan por debajo de 1")

"""
---------------------
INCISO B)
---------------------
"""
print('------------------------')
print('INCISO B)')
print('------------------------')


import pandas as pd
import numpy as np

# Especifica la ruta de tu archivo CSV
file_name = 'D:\\INFORMATICA\\1 - 2024\\INF 354\\sunpots.csv'

# Leer los datos directamente con pandas, especificando el delimitador adecuado
df_sunspots = pd.read_csv(file_name, delimiter=';')

# Paso 3: Calcular Q3 y el percentil 80 por columna
q3 = df_sunspots.quantile(0.75)  # Tercer cuartil (Q3)
p80 = df_sunspots.quantile(0.80)  # Percentil 80



# Paso 4: Explicar significado
#print("Tercer cuartil (Q3) - Significado:")
#print("El tercer cuartil (Q3) es el valor por debajo del cual se encuentran los 75% de los datos en cada columna.")
print(q3)

#print("\nPercentil 80 - Significado:")
#print("El percentil 80 es el valor por debajo del cual se encuentran los 80% de los datos en cada columna.")
print(p80)



"""
---------------------
INCISO C)
---------------------
"""
print('------------------------')
print('INCISO C)')
print('------------------------')



import pandas as pd
import numpy as np

# Especifica la ruta de tu archivo CSV
file_name = 'D:\\INFORMATICA\\1 - 2024\\INF 354\\sunpots.csv'

# Leer los datos directamente con pandas, especificando el delimitador adecuado
df_sunspots = pd.read_csv(file_name, delimiter=';')

# Calcular la media aritmética de cada columna numérica
media_aritmetica = df_sunspots.mean()

# Calcular la mediana de cada columna numérica
mediana = df_sunspots.median()

# Calcular la moda de cada columna (solo se aplica a datos categóricos o discretos)
moda = df_sunspots.mode()

# Calcular la media geométrica de cada columna numérica
# Pandas no tiene una función incorporada para calcular la media geométrica, pero podemos usar numpy
media_geometrica = np.exp(df_sunspots.apply(np.log).mean())

# Mostrar los resultados
print("Media aritmética:")
print(media_aritmetica)

print("\nMediana:")
print(mediana)

print("\nModa:")
print(moda)

print("\nMedia geométrica:")
print(media_geometrica)

print("La media se calcula sumando todos los valores, la mediana indica el valor central de todos los datos,\n"
      " la moda indica el valor mas comun, la media geometrica aplica para datos que varian multiplicativamente, \n")

print("Para un articulo cientifico, es común reportar la media y la mediana para proporcionar\n"
      " una visión completa de la distribución de los datos.")



"""
---------------------
INCISO D)
---------------------
"""
print('------------------------')
print('INCISO D)')
print('------------------------')


#instalando la biblioteca

import pandas as pd
import matplotlib.pyplot as plt

# Especifica la ruta de tu archivo CSV
file_name = 'D:\\INFORMATICA\\1 - 2024\\INF 354\\sunpots.csv'

# Leer los datos directamente con pandas, especificando el delimitador adecuado
df_sunspots = pd.read_csv(file_name, delimiter=';')

# Asumiendo que tienes fechas en una columna y datos numéricos en otra para graficar
# Supongamos que 'fecha' es la columna de fechas y 'dato' es la columna de datos numéricos




# Año vs Mes

plt.figure(figsize=(10, 5))  # Ajusta el tamaño del gráfico si es necesario
plt.plot(df_sunspots['Y'], df_sunspots['M'], marker='o')  # Asume
plt.title('Gráfico de datos de manchas solares')  # Título del gráfico
plt.xlabel('AÑO')  # Nombre del eje x
plt.ylabel('MES')  # Nombre del eje y
plt.grid(True)  # Agrega una cuadrícula al gráfico
plt.show()  # Muestra el gráfico

# Año vs Dia

plt.figure(figsize=(10, 5))  # Ajusta el tamaño del gráfico si es necesario
plt.plot(df_sunspots['Y'], df_sunspots['D'], marker='o')  # Asume
plt.title('Gráfico de datos de manchas solares')  # Título del gráfico
plt.xlabel('AÑO')  # Nombre del eje x
plt.ylabel('DIA')  # Nombre del eje y
plt.grid(True)  # Agrega una cuadrícula al gráfico
plt.show()  # Muestra el gráfico

# Año vs DTS

plt.figure(figsize=(10, 5))  # Ajusta el tamaño del gráfico si es necesario
plt.plot(df_sunspots['Y'], df_sunspots['DTS'], marker='o')  # Asume
plt.title('Gráfico de datos de manchas solares')  # Título del gráfico
plt.xlabel('AÑO')  # Nombre del eje x
plt.ylabel('DTS')  # Nombre del eje y
plt.grid(True)  # Agrega una cuadrícula al gráfico
plt.show()  # Muestra el gráfico

# Año vs DE

plt.figure(figsize=(10, 5))  # Ajusta el tamaño del gráfico si es necesario
plt.plot(df_sunspots['Y'], df_sunspots['DE'], marker='o')  # Asume
plt.title('Gráfico de datos de manchas solares')  # Título del gráfico
plt.xlabel('AÑO')  # Nombre del eje x
plt.ylabel('DESVIACION ESTANDAR')  # Nombre del eje y
plt.grid(True)  # Agrega una cuadrícula al gráfico
plt.show()  # Muestra el gráfico

# Año vs #OBS

plt.figure(figsize=(10, 5))  # Ajusta el tamaño del gráfico si es necesario
plt.plot(df_sunspots['Y'], df_sunspots['#OBS'], marker='o')  # Asume
plt.title('Gráfico de datos de manchas solares')  # Título del gráfico
plt.xlabel('AÑO')  # Nombre del eje x
plt.ylabel('NUMERO DE OBSERVACIONES')  # Nombre del eje y
plt.grid(True)  # Agrega una cuadrícula al gráfico
plt.show()  # Muestra el gráfico

# Año vs #IN

plt.figure(figsize=(10, 5))  # Ajusta el tamaño del gráfico si es necesario
plt.plot(df_sunspots['Y'], df_sunspots['IN'], marker='o')  # Asume
plt.title('Gráfico de datos de manchas solares')  # Título del gráfico
plt.xlabel('AÑO')  # Nombre del eje x
plt.ylabel('INDICADOR PROVISIONAL')  # Nombre del eje y
plt.grid(True)  # Agrega una cuadrícula al gráfico
plt.show()  # Muestra el gráfico

