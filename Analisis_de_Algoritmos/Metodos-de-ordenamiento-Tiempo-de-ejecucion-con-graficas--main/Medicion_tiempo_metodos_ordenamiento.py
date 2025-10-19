# benchmark_ordenamientos.py
# Programa principal para medir el tiempo de ejecución de varios algoritmos de ordenamiento
# y guardar los resultados en un archivo CSV.

import metodos_ordenamiento
import random as rn
from time import perf_counter
import os
import sys
import csv # Importado para el manejo robusto de archivos CSV

# Si el script se ejecuta en un entorno que no es interactivo (como algunos canvas), 
# las llamadas a input() pueden fallar.
# Se añade una función stub para manejar esto.
def safe_input(prompt):
    """Maneja la entrada de usuario de forma segura."""
    try:
        return input(prompt)
    except EOFError:
        # Esto ocurre cuando la entrada no es un TTY, por ejemplo, en entornos automatizados.
        print(f"\nEntrada no interactiva: {prompt.strip()} se omite.")
        return ""


# Diccionario: nombre → función del módulo
METODOS = {
    "burbuja": metodos_ordenamiento.burbuja,
    "insercion": metodos_ordenamiento.insercion,
    "mezcla": metodos_ordenamiento.mezcla,
    "quicksort": metodos_ordenamiento.quikcsort,
    "seleccion": metodos_ordenamiento.seleccion
}

def crear_lista(longitud, limite_valor=200):
    """Genera lista de enteros aleatorios"""
    return [rn.randint(0, limite_valor) for _ in range(longitud)]

def pedir_entero(mensaje, default):
    """Pide un número entero al usuario con valor por defecto"""
    try:
        entrada = safe_input(f"{mensaje} [{default}]: ").strip()
        return int(entrada) if entrada else default
    except ValueError:
        print(f"Entrada inválida, usando {default}")
        return default
    
    
if __name__ == "__main__":
    
    while True:
        print("== Benchmark de algoritmos de ordenamiento ==")
        print("Métodos disponibles:", ", ".join(METODOS.keys()))
    
        # pedir método
        metodo_nombre = safe_input("Elige un método: ").strip().lower()
        if metodo_nombre not in METODOS:
            print("Método inválido. Usa uno de:", ", ".join(METODOS.keys()))
            continue  # Vuelve al inicio del while
        
        metodo_funcion = METODOS[metodo_nombre]

        # pedir tamaño máximo de lista
        max_size = pedir_entero("Tamaño máximo de la lista", 5000)
        # pedir paso
        step = pedir_entero("Paso entre pruebas", 1000)
        if step <= 0:
            print("Paso inválido. Se usará 1000 por defecto.")
            step = 1000

        # pedir nombre archivo
        archivo_nombre = safe_input(f"Nombre del archivo CSV [{metodo_nombre}.csv]: ").strip()
        if not archivo_nombre:
            archivo_nombre = f"{metodo_nombre}.csv"
        
        # Corrección: Aseguramos que el archivo se guarde en la ruta correcta.
        # En entornos normales, esto ya está en el directorio del script.
        # En el canvas, se asume que los archivos se crean donde se ejecuta el script.
        
        # generar lista base
        print(f"\nGenerando lista base de {max_size} elementos aleatorios...")
        lista = crear_lista(max_size) 
        
        # medir tiempos y guardar en archivo
        print(f"Midiendo tiempo de ejecución para {metodo_nombre}...")
        try:
            with open(archivo_nombre, "w", newline="") as archivo:
                # Usamos csv.writer para garantizar el formato correcto (delimitador ;)
                # y la compatibilidad con el módulo Graficador_datos_vs_tiempo.
                escritor = csv.writer(archivo, delimiter=';') 
                
                # Escribir encabezado CSV
                escritor.writerow(["N", "Tiempo"])
                
                for n in range(step, max_size + 1, step):
                    # Clonar la lista para asegurar que el algoritmo de ordenamiento
                    # no afecte al benchmark (esto es crucial).
                    lista_nueva = lista[:n]  
                    
                    inicio = perf_counter()
                    metodo_funcion(lista_nueva)
                    tiempo = perf_counter() - inicio
                    
                    # Escribir resultados usando el escritor CSV
                    # n es el tamaño, y el tiempo se formatea a 5 decimales como string
                    escritor.writerow([n, f"{tiempo:.5f}"]) 
                    print(f"{metodo_nombre:10s} | N={n:6d} | Tiempo={tiempo:.5f} s")

            print(f"\nResultados guardados en: {os.path.abspath(archivo_nombre)}")
        
        except IOError as e:
            print(f"Error al escribir en el archivo {archivo_nombre}: {e}")
            
        # Preguntar si desea salir o continuar con otro benchmark
        continuar_resp = safe_input("\n¿Quieres realizar otro benchmark? (s/n): ").strip().lower()
        if continuar_resp != "s":
            break # Sale del while True para ir a la parte de la gráfica

# Lógica para graficar
resp = safe_input("\n¿Quieres graficar resultados ahora? (s/n): ").strip().lower()
if resp == "s":
    try:
        import Graficador_datos_vs_tiempo
        # Iniciar la interfaz gráfica de Tkinter
        Graficador_datos_vs_tiempo.iniciar_graficador()
    except ImportError:
        print("Error: No se pudo importar el módulo Graficador_datos_vs_tiempo.py. Asegúrate de que existe.")
    except Exception as e:
        print(f"Ocurrió un error al intentar graficar: {e}")
