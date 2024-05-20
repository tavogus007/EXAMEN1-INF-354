# -*- coding: utf-8 -*-
"""
Created on Sat May 18 17:32:08 2024

@author: GustavoGutierrez
"""

"""
import sys
print(sys.executable)
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
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    return data

# Especifica la ruta de tu archivo CSV
file_name = 'D:\\INFORMATICA\\1 - 2024\\INF 354\\sunpots_completo_con_comas.csv'

# Leer los datos
dataset = leer_datos(file_name)



"""
---------------------
IMPUTACION DE VALORES FALTANTES
---------------------
"""

print("PRIMER ALGORITMO")

import pandas as pd
import numpy as np

# Cargar los datos
file_path = 'D:\\INFORMATICA\\1 - 2024\\INF 354\\sunpots_completo_con_comas.csv'
df = pd.read_csv(file_path)

# Reemplazar -1 por NaN
df.replace(-1, np.nan, inplace=True)

# Imputar los valores faltantes con la media de la columna
df['DTS'].fillna(df['DTS'].mean(), inplace=True)

print(df)

print("Dado que el conjunto de datos tiene valores faltantes representados por -1,\n"
      "es importante imputar estos valores para no afectar el análisis.\n" 
      "Razón de uso: La imputación de valores faltantes es crucial para mantener \n"
      "la integridad del análisis, ya que los algoritmos de aprendizaje automático no pueden manejar valores faltantes directamente.")


"""
---------------------
ONEHOTENCODER PARA EL MES
---------------------
"""

print("SEGUNDO ALGORITMO")

from sklearn.preprocessing import OneHotEncoder

# Convertir dataset a DataFrame de pandas
df = pd.DataFrame(dataset)

# Asegurarse de que los datos numéricos estén en el tipo correcto
df['M'] = pd.to_numeric(df['M'])


# Crear el OneHotEncoder
one_hot_encoder = OneHotEncoder()

# Aplicar OneHotEncoder a la columna M
mes_encoded = one_hot_encoder.fit_transform(df[['M']]).toarray()

# Crear un DataFrame de las columnas OneHotEncoded
mes_encoded_df = pd.DataFrame(mes_encoded, columns=one_hot_encoder.get_feature_names_out(['M']))

# Unir el DataFrame original con el DataFrame OneHotEncoded
df = pd.concat([df, mes_encoded_df], axis=1).drop(['M'], axis=1)

print(df)

import sklearn
print(sklearn.__version__)



print("OneHotEncoding es útil para convertir variables categóricas en un formato\n"
       "que puede ser utilizado por algoritmos de aprendizaje automático que requieren entrada numérica.")


"""
---------------------
ESCALADO DE DATOS
---------------------
"""

print("TERCER ALGORITMO")

from sklearn.preprocessing import StandardScaler

# Crear el escalador
scaler = StandardScaler()

# Aplicar el escalado a la columna 'DTS'
df['DTS'] = scaler.fit_transform(df[['DTS']])

print(df)

print("El escalado es importante para algoritmos que son sensibles a la escala de los datos, \n"
      "como regresión lineal y redes neuronales.")


"""
---------------------
NORMALIZACION MIN-MAX
---------------------
"""

print("CUARTO ALGORITMO")

from sklearn.preprocessing import MinMaxScaler

# Crear el normalizador
min_max_scaler = MinMaxScaler()

# Aplicar la normalización a la columna 'DTS'
df['DTS'] = min_max_scaler.fit_transform(df[['DTS']])

print(df)

print("La normalización Min-Max es útil para algoritmos que no hacen suposiciones sobre la distribución \n"
      "de los datos y requieren que todos los valores estén en un rango uniforme.")


"""
---------------------
CODIFICACION BINARIA
---------------------
"""

print("QUINTO ALGORITMO")

from sklearn.preprocessing import LabelBinarizer

# Crear el codificador binario
binarizer = LabelBinarizer()

# Aplicar la codificación binaria a la columna 'IN'
df['IN'] = binarizer.fit_transform(df['IN'])

print(df)

print("La codificación binaria reduce la dimensionalidad en comparación con OneHotEncoder, lo que \n"
      "puede ser beneficioso para conjuntos de datos con muchas categorías.")


