# -*- coding: utf-8 -*-
"""
Created on Sun May 19 01:42:48 2024

@author: GustavoGutierrez
"""


import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido (las relaciones familiares tienen dirección)
G = nx.DiGraph()

# Añadir miembros de la familia como nodos
G.add_node("Andres Gaspar")  #Abuelo
G.add_node("Yolanda Gaspar") #Abuela
G.add_node("Sandra Gaspar") #tio
G.add_node("Roberto Gutierrez") # padre
G.add_node("Tania Mirza") #madre
G.add_node("Gustavo Gutierrez") # hijo
G.add_node("Carolina Gutierrez") #hija 
G.add_node("Jean Rada") #primo
G.add_node("Samara Rada") #prima

# Añadir relaciones familiares como aristas (edges)
G.add_edge("Andres Gaspar", "Tania Mirza")
G.add_edge("Yolanda Gaspar", "Tania Mirza")
G.add_edge("Andres Gaspar", "Sandra Gaspar")
#G.add_edge("Abuela", "Tío")
G.add_edge("Roberto Gutierrez", "Gustavo Gutierrez")
G.add_edge("Roberto Gutierrez", "Carolina Gutierrez")
G.add_edge("Tania Mirza", "Gustavo Gutierrez")
G.add_edge("Tania Mirza", "Carolina Gutierrez")
G.add_edge("Sandra Gaspar", "Jean Rada")
G.add_edge("Sandra Gaspar", "Samara Rada")

# Visualización del grafo
plt.figure(figsize=(10, 8))  # Tamaño de la figura
pos = nx.spring_layout(G)   # Algoritmo para distribuir los nodos
nx.draw_networkx(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=12, font_weight="bold", arrowsize=20)  # Dibuja el grafo
plt.title("Árbol Genealógico")  # Título
plt.show()                   # Mostrar el gráfico





















"""
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout 

# Crear un grafo dirigido (las relaciones familiares tienen dirección)
G = nx.DiGraph()

# Añadir miembros de la familia como nodos
G.add_node("Andres Gaspar")  #Abuelo
G.add_node("Yolanda Gaspar") #Abuela
G.add_node("Sandra Gaspar") #tio
G.add_node("Roberto Gutierrez") # padre
G.add_node("Tania Mirza") #madre
G.add_node("Gustavo Gutierrez") # hijo
G.add_node("Carolina Gutierrez") #hija 
G.add_node("Jean Rada") #primo
G.add_node("Samara Rada") #prima

# Añadir relaciones familiares como aristas (edges)
G.add_edge("Andres Gaspar", "Tania Mirza")
G.add_edge("Yolanda Gaspar", "Tania Mirza")
G.add_edge("Andres Gaspar", "Sandra Gaspar")
#G.add_edge("Abuela", "Tío")
G.add_edge("Roberto Gutierrez", "Gustavo Gutierrez")
G.add_edge("Roberto Gutierrez", "Carolina Gutierrez")
G.add_edge("Tania Mirza", "Gustavo Gutierrez")
G.add_edge("Tania Mirza", "Carolina Gutierrez")
G.add_edge("Sandra Gaspar", "Jean Rada")
G.add_edge("Sandra Gaspar", "Samara Rada")

# Visualización mejorada con graphviz_layout
plt.figure(figsize=(10, 8))
pos = graphviz_layout(G, prog="dot")  # Cambiar el algoritmo de diseño
nx.draw_networkx(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=12, font_weight="bold", arrowsize=20)
plt.title("Árbol Genealógico")
plt.show()

"""