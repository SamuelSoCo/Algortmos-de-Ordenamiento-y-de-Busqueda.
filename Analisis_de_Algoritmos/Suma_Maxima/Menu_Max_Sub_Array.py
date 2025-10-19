# Archivo: menu_simple.py

"""Este es un menu basico para el Algoritmo de Kanade's y sus tres versiones para mostrar el tiempo que tarda en
terminar cada funcion y ver cual es la mas optima"""

# Libreria y importacion del archivo
import time
from Max_Sub_Array import maxsuma1, maxsuma2, maxsuma3

# Funcion para medir el tiempo de ejecucion de cada funcion llamandola y dandole una lista que introduce el usuario
def medir_tiempo_ejecucion(funcion, lista):
    """
    Ejecuta la funcion y mide el tiempo. Espera que la funcion devuelva (suma, sub_array).
    """
    inicio = time.perf_counter()
    # Desempaquetamos los dos valores que devuelven las funciones modificadas
    suma, sub_array = funcion(lista) 
    fin = time.perf_counter()
    tiempo = (fin - inicio) * 1000  # para convertirlo a milisegundos
    
    return suma, sub_array, tiempo  # Devuelve la suma, el sub-array y el tiempo

# Funcion para pedir la lista al usuario
def pedir_lista():
    while True:
        entrada = input(" Ingrese una lista de numeros(Ejemplo 2,-5,6,4,-2): ")
        try:
            # Corrección: Transforma la entrada separada por comas en una lista de enteros.
            lista = [int(x.strip()) for x in entrada.split(',') if x.strip()]
            return lista
        except ValueError:
            print(" La lista es invalida, ingrese una lista como en el ejemplo.")
            
# Funcion para el menu
def menu():  # ejecutamos los 3 algoritmos y se compara
    print("=====================================================")
    print("  ALGORTIMO DE KANADE'S O MAXIMO SUBARREGLO.         ")
    print("=====================================================")
    
    lista = pedir_lista()
    
    if not lista:
        print("La lista esta vacia. Cerrando programa.")
        return
        
    print(f"\nLa lista ingresada tiene {len(lista)} elementos y es:\n{lista}\n")
    
    # Definición de las funciones a ejecutar
    funciones = [
        ("Versión 1 (O(n))", maxsuma1),
        ("Versión 2 (2 For)", maxsuma2),
        ("Versión 3 (3 For)", maxsuma3)
    ]
    
    
    print(f"{'Algoritmo':<20} | {'Suma Máxima':<15} | {'Tiempo (ms)':<15} | {'Sub-Arreglo Máximo'}")
    print("-" * 85)

    for nombre, funcion in funciones:
        # Aquí se desempaquetan los 3 valores (suma, sub_array, tiempo)
        suma, sub_array, tiempo = medir_tiempo_ejecucion(funcion, lista)
        
        # Mostrar el resultado
        print(f"{nombre:<20} | {suma:<15} | {tiempo:15.6f} | {str(sub_array)}")
    
    print("-" * 85)
    print("\nEl Algoritmo de la Versión 1 (Kadane's) siempre será el más rápido (O(n)).")

if __name__ == "__main__":
    menu()


""" Lista usada como prueba contiene 100 elementos del -50 al 50
16,14,48,-46,-17,-43,15,-40,-41,31,19,25,36,44,-10,-20,-48,46,-28,-11,27,33,-35,5,49,-38,36,-27,-19,-38,-47,-13,-48,27,11,
-36,36,29,19,43,-11,-24,-35,-19,27,-38,-28,15,31,-3,19,4,30,-26,-36,44,-44,19,10,32,-27,-10,13,32,49,-39,26,48,-41,-4,37,13,-36,-31,
-34,36,-41,36,-27,47,-38,-49,27,14,24,-45,-14,-37,29,-36,48,42,-22,12,36,44,14,-41,47,-32"""