# Archivo: Max_Sub_Array.py

"""Algortimos del problema de Kanade's para el maximo sud array de una lista de numeros."""

# Version 1 Un solo For algoritmo lineal. (O(n))

def maxsuma1(lista):
    """
    
    Versión 1: Algoritmo de Kadane's (Lineal O(n)).
    Que devuelve  la suma maxima del subarreglo y el sub-arreglo.
    No maneja listas con elementos negativos por lo que devolvería 0 y [] si la suma máxima real es negativa.
    """
    max_global = 0  # Almacenara la suma maxima encontrada hasta el momento
    suma_actual = 0 # Almacena la suma del subarray actual
    
    # Índices para rastrear el sub-arreglo
    inicio_temp = 0
    inicio_max = 0
    fin_max = -1  # Inicializado a -1 para listas vacías o donde el máximo sea 0

    for i, num in enumerate(lista):
        suma_actual += num
        
        # Si la suma actual se vuelve negativa en un ciclo la reiniciaremos a 0 
        if suma_actual < 0:
            suma_actual = 0
            inicio_temp = i + 1 # El próximo elemento sería el inicio de un nuevo sub-arreglo
            
        # Actualizamos max si la suma actual es mayor al máximo global
        if suma_actual > max_global:
            max_global = suma_actual
            inicio_max = inicio_temp
            fin_max = i
            
    # Caso especial: Si el resultado es 0, puede ser una lista de solo negativos que devolvió 0.
    # El sub-arreglo es el slice: lista[inicio_max : fin_max + 1]
    sub_array_max = lista[inicio_max : fin_max + 1]
    
    return max_global, sub_array_max # Retorna (suma, sub_array)


# Algoritmo version 2 sin ordenar, O(n^2) con bucles anidados
def maxsuma2(lista):
    
    n = len(lista)
    if n == 0:
        return 0, []
    
    max_global = 0 # Almacena la suma maxima global encontrada
    inicio_max = 0
    fin_max = -1
    
    # Bucle exterior itera sobre el final de los posibles subarrays (indice j)
    for i in range(n):
        suma_actual = 0 # variable auxiliar para la suma del subarray que empieza en 'i' 
        
        # Bucle interior para definir el punto final 'j' del subarray
        for j in range(i, n):
            suma_actual += lista[j] # acumulara la suma de lista[i.....j]
            
            if suma_actual > max_global:
                max_global = suma_actual
                inicio_max = i
                fin_max = j # El índice actual 'j' es el final
                
    sub_array_max = lista[inicio_max : fin_max + 1]
    
    # Manejo del caso donde la suma máxima es 0 (lista de solo negativos o vacía)
    if max_global == 0 and n > 0 and fin_max == -1:
        return 0, []
        
    return max_global, sub_array_max # Retorna (suma, sub_array)


# Version 3 algoritmo con 3 bucles (O(n^3))
def maxsuma3(lista):
    n = len(lista)
    if n == 0:
        return 0, []
    
    max_global = 0
    inicio_max = 0
    fin_max = -1
    
    # Bucle exterior para definir el inicio del subarray 'i'
    for i in range(n):
        # En este segundo for define el punto final del subarray 'j'
        for j in range(i, n):
            suma_actual = 0 # Es la suma del subarray actual desde 'i' hasta 'j'
            
            # Tercer for para realisar todas las sumas de los elementos desde 'i' hasta'j'
            for k in range(i, j + 1):
                suma_actual += lista[k]
                
            # comparamos la suma del subarray actual con la suma maxima encontrada hasta el momento
            if suma_actual > max_global:
                max_global = suma_actual
                inicio_max = i
                fin_max = j
                
    sub_array_max = lista[inicio_max : fin_max + 1]
    
    if max_global == 0 and n > 0 and fin_max == -1:
        return 0, []
        
    return max_global, sub_array_max # Retorna (suma, sub_array)


if __name__ == "__main__":
    
        
        #Ejemplo de uso de maxsuma1
        """Usaremos la lista 27,6,-50,21,-3,14,16,-8,42,33,-21,9 el resultado de la suma es 115 y el subarreglo maximo es 21,-3,14,16,-8,42,33"""
        
        lista=[27,6,-50,21,-3,14,16,-8,42,33,-21,9]
        print(f"Version (1) lineal del Problema del Maximo SubArray:")
        print(f"Lita usada en el ejemplo de uso {lista}")
        suma1,sub1=maxsuma1(lista)
        print(f"Suma maxima:{suma1}\nSubArray Maximo:{sub1}")
        
        """--------------------------------------------------------
        Ejemplo de uso de maxsuma2 uso de for anidados """
        
        print("\n")
        print(f"Version (2) con for anidados sin ordenar del Problema del Maximo SubArray:")
        print(f"Lista usada en el ejemplo:{lista}")
        suma2,sub2=maxsuma1(lista)
        print(f"Suma maxima:{suma2}\nSubArray Maximo:{sub2}")
        
        
        """------------------------------------------------------------------
        Ejemplo de uso de maxsuma3 tres for"""
        print("\n")
        print(f"Version (3) con uso de 3 for.")
        print(f"Lista usada en el ejemplo {lista}")
        suma3,sub3=maxsuma1(lista)
        print(f"Suma maxima:{suma3}\nSubArray Maximo:{sub3}")
        
    
    
