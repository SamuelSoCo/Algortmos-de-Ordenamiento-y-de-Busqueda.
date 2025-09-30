"""Programa para encontrar la ruta más rápida de una estación a otra de las líneas del metro de
la CDMX donde usaremos la biblioteca NETWORKX para crear un grafo y encontrar la ruta más corta.
Usaremos pandas y numpy, y el CSV será convertido a un DataFrame para poderlo usar en el grafo."""


#IMPORTACIÓN DE LIBRERÍAS

import pandas as pd
import numpy as np 
import networkx as nx 
import matplotlib.pyplot as plt


#LECTURA DEL ARCHIVO CSV

# El archivo CSV debe contener columnas: Origen, Destino y Tiempo
# "Origen"  -> Estación de inicio
# "Destino" -> Estación de llegada
# "Tiempo"  -> Tiempo estimado entre ambas estaciones

df = pd.read_csv(
    r"C:\Users\samue\OneDrive\Escritorio\CURSOS\python\Estaciones_del_metro.csv",
    index_col=None,
    encoding="latin1"
)

#CREACIÓN DEL GRAFO

# Usamos la función from_pandas_edgelist de NetworkX:
# - source: columna que indica la estación de origen
# - target: columna que indica la estación de destino
# - edge_attr: atributo de la arista (en este caso, el tiempo)

METRO = nx.from_pandas_edgelist(df, source='Origen', target='Destino', edge_attr='Tiempo')

#MENÚ DE ENTRADA PARA EL USUARIO

print("===== METRO CDMX - RUTA MÁS CORTA =====")
print("Escribe el nombre exacto de la estación como aparece en el archivo CSV.")
print("Ejemplo: Pantitlan, Tacubaya, Salto del Agua")
print("Usa mayúsculas iniciales y minúsculas en los conectores como 'de', 'del', 'la'.\n")

# Pedimos al usuario el origen y el destino
origen = input("Ingresa la estación de origen: ")
destino = input("Ingresa la estación de destino: ")

#VALIDACIÓN DE LAS ESTACIONES

# Verificamos que las estaciones ingresadas existan en el grafo
# Si alguna no existe, se muestra un mensaje de error

if origen not in METRO.nodes() or destino not in METRO.nodes():
    print("\nAlguna de las estaciones ingresadas no existe en el METRO CDMX.")
else:
    try:
        
        #CÁLCULO DE LA RUTA MÁS CORTA
        
        # Usamos el algoritmo de Dijkstra con la función dijkstra_path:
        # - METRO  : el grafo con todas las estaciones
        # - source : estación de origen
        # - target : estación de destino
        # - weight : atributo usado como peso (el tiempo de viaje)
        
        ruta = nx.dijkstra_path(METRO, source=origen, target=destino, weight="Tiempo")
        
        # También obtenemos la suma total de los tiempos en la ruta
        tiempo_total = nx.dijkstra_path_length(METRO, source=origen, target=destino, weight="Tiempo")

        print("\nLa ruta más corta encontrada es:")
        print(" -> ".join(ruta))
        print(f"Tiempo total estimado: {tiempo_total} minutos")

        
        #CREACIÓN DEL SUBGRAFO
        
        # El subgrafo contendrá únicamente las estaciones de la ruta más corta
        # Esto facilita la visualización gráfica
        
        subgrafo = METRO.subgraph(ruta)

        
        #VISUALIZACIÓN DEL SUBGRAFO
        
        # Usamos matplotlib para dibujar el subgrafo
        # - node_color : color de los nodos
        # - node_size  : tamaño de los nodos
        # - font_size  : tamaño de las etiquetas
        # - edge_color : color de las aristas
        # - width      : grosor de las aristas
        
        plt.figure(figsize=(10,6))
        pos = nx.spring_layout(subgrafo, seed=42)
        nx.draw(
            subgrafo, pos,
            with_labels=True,
            node_color="lightblue",
            node_size=800,
            font_size=10,
            edge_color="red",
            width=2
        )

        # Mostramos las etiquetas con el tiempo en cada arista
        etiquetas = nx.get_edge_attributes(subgrafo, "Tiempo")
        nx.draw_networkx_edge_labels(subgrafo, pos, edge_labels=etiquetas, font_size=9)

        # Título del gráfico
        plt.title(f"Ruta más corta de {origen} a {destino}")
        plt.show()

    except Exception as e:
        print(f"\nError al calcular la ruta más corta: {e}")
