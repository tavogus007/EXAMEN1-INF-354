#Con el mismo dataset recortado (sunpots_menos_datos.csv) 
#porque la original no se visualiza bien


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt
import io
import pydot

df = pd.read_csv('D:\\INFORMATICA\\1 - 2024\\INF 354\\sunpots_menos_datos.csv')

from sklearn.model_selection import train_test_split

# Dividir datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(df.drop('VAL', axis=1), df['VAL'], test_size=0.2, random_state=42)

# Crear modelo de árbol de decisión
clf = DecisionTreeClassifier(random_state=42)

# Entrenar modelo con conjunto de entrenamiento
clf.fit(X_train, y_train)

# Graficar árbol de decisión
dot_data = io.StringIO()
tree.export_graphviz(clf, out_file=dot_data)
graph = pydot.graph_from_dot_data(dot_data.getvalue())[0]
graph.write_png('sunpots_tree.png')
plt.imshow(plt.imread('sunpots_tree.png'))
plt.show()