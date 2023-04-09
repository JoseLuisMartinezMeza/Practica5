

# Importamos la librerías
import networkx as nx
import matplotlib.pyplot as plt

# Creamos un grafo vacío
G = nx.Graph()

# Añadimos los nodos del 1 al 6
G.add_nodes_from([1, 2, 3, 4, 5, 6])

# Añadimos las aristas con sus pesos
G.add_edge(1, 2, weight=3)
G.add_edge(1, 3, weight=4)
G.add_edge(1, 4, weight=5)
G.add_edge(2, 3, weight=6)
G.add_edge(2, 5, weight=2)
G.add_edge(3, 4, weight=7)
G.add_edge(3, 5, weight=8)
G.add_edge(3, 6, weight=9)
G.add_edge(4, 6, weight=10)
G.add_edge(5, 6, weight=11)

# Dibujamos el grafo original con los pesos de las aristas
nx.draw(G, with_labels=True)
nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G))
plt.show()

# Aplicamos el algoritmo de Kruskal para obtener el árbol de mínimo coste
T = nx.minimum_spanning_tree(G)

# Dibujamos el árbol resultante con los pesos de las aristas
nx.draw(T, with_labels=True)
nx.draw_networkx_edge_labels(T, pos=nx.spring_layout(T))
plt.show()

# Calculamos el peso total del árbol
total_weight = sum([T[u][v]['weight'] for u, v in T.edges()])
print(f"El peso total del árbol es {total_weight}")