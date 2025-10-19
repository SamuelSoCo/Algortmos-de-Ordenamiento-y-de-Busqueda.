
#Metodo burbuja
def burbuja(lista):
    n=len(lista)
    for i in range(n):
        for j in range(0,n-i-1):
            #intercambio de valores
            if lista[j] >=lista[j+1]:
                lista[j],lista[j+1]=lista[j+1],lista[j]
    return lista




#Metodo de ordenamiento por Seleccion (selection sort)

def seleccion(lista):
    n = len(lista)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        # Intercambio
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    return lista



def insercion(lista3: list) -> list:
    """
    Ordenamiento por inserción (modifica 'lista' en sitio).
    También devuelve la misma referencia para permitir:
    lista = insercion(lista)  o  insercion(lista)
    """
    lista=lista3.copy()
    for indice_actual in range(1, len(lista)):
        valor_actual = lista[indice_actual]
        posicion = indice_actual - 1
        # desplazamos los elementos mayores una posición a la derecha
        while posicion >= 0 and lista[posicion] > valor_actual:
            lista[posicion + 1] = lista[posicion]
            posicion -= 1
        lista[posicion + 1] = valor_actual
    return lista

    


#Ordenamiento por Mezcla(merge sort)



def mezcla(lista4: list) -> list:
    """
    .
    Modifica 'lista' directamente y además la devuelve.
    """
    lista=lista4.copy()
    if len(lista) <= 1:
        return lista  # caso base: ya está ordenada

    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]

    # Ordenar recursivamente cada mitad
    izquierda = mezcla(izquierda)
    derecha = mezcla(derecha)

    # Mezclar de vuelta en 'lista'
    i = j = k = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            lista[k] = izquierda[i]
            i += 1
        else:
            lista[k] = derecha[j]
            j += 1
        k += 1

    # Agregar los restos de izquierda (si quedan)
    while i < len(izquierda):
        lista[k] = izquierda[i]
        i += 1
        k += 1

    # Agregar los restos de derecha (si quedan)
    while j < len(derecha):
        lista[k] = derecha[j]
        j += 1
        k += 1

    return lista

        

#Ordenamiento rapido o Quick sort

def quikcsort(lista5:list)->list:
    lista=lista5.copy()
    if len(lista)<=1:
        return lista
    else:
        pivote=lista[0]
        menores=[x for x in lista[1:] if x<= pivote]
        mayores=[x for x in lista[1:] if x>pivote]
        return quikcsort(menores)+[pivote]+quikcsort(mayores)
    


# Bloque de pruebas (solo si ejecutas este archivo directamente)
if __name__ == "__main__":
        
 #Ejemplo de uso de Burbuja
 lista1=[3,6,8,9,2,1,2]
 print("Lista antes del ordenamiento: ",lista1)
 lista1.append(10)
 print(f"Se añadio en la lista el numero 10 y la lista despues de burbuja es:{burbuja(lista1)}")

 #Ejemplo de uso de seleccion
 print("\n")
 print("\n")

 lista2=[44,3,2,55,6,4,7]
 print(f"Lista antes del ordenamiento: {lista2}")
 lista2.append(30)
 print(f"Lista despues del uso del metodo seleccion del numero 30:{seleccion(lista2)}")

 #Metodo por insercion
 print("\n")
 print("\n")

 #Ejemplo de uso de insercion

 lista3=[44,2,4,7,2,45,67,86,90]
 print(f"La lista antes de  aplicar el metodo de ordenamineto insercion:{lista3}")
 ordenada_mezcla=insercion(lista3)
 print(f"Lista despues del metodo inserccion:{ordenada_mezcla}")#
 print("La lista original no fue modificada",lista3)
 #podemos usarla en este caso sin modificar la lista original si lo pasamos en una variable

 print("\n")
 print("\n")

 #Uso de ejemplo del ordenamiento por mezcla
 lista4=[44,6,3,12,5,77,9,54,34,35]
 print(f"La lista despues del metodo de ordenamiento mezcla:{mezcla(lista4)}")
 print("La lista original es:",lista4)

 print("\n")
 print("\n")

 #Ejemplo de uso de quicksort
 lista5=[44,22,6,7,23,54,2003,23,12,4,1]
 print(f"La lista despues del metodo de ordenamineto Quick Sort:{quikcsort(lista5)}")
 print("La lista origninal es:",lista5)


