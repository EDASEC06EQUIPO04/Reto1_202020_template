import config as cf
from ADT import list as lt
from Sorting.insertionsort import lessfunction

def lessfunction (elemento1, elemento2):
    if elemento1<elemento2:
      return True
    return False

def shellSort(lst, lessfunction):
    n = lt.size(lst)
    h = 1
    while h < n/3:          # Se calcula el tamaño del primer gap. La lista se h-ordena con este tamaño
        h = 3*h + 1         # por ejemplo para n = 100, h toma un valor inical de 13 , 4, 1
    while (h >= 1):
        for i in range (h,n):
            j = i
            while (j>=h) and lessfunction (lt.getElement(lst,j+1),lt.getElement(lst,j-h+1)):
                lt.exchange (lst, j+1, j-h+1)
                j -=h
        h //=3              # h se decrementa en un tercio. cuando h es igual a 1, se comporta como insertionsort


lista=lt.newList  ()
lt.addFirst(lista,200)
lt.insertElement(lista,34,1)
lt.insertElement(lista,44,2)
lt.insertElement(lista,45,3)
lt.insertElement(lista,34,4)
lt.insertElement(lista,99,5)

shellSort(lista,lessfunction)
print ("Estamos haciendo una prueba de uso de la estructura de datos List de tipo Single linked list")
print (lista)
print ("+++++++++++++++++++++++++++++++++++++++++++++++++")
input ("Clic para continuar con el tipo ARRAY LIST ...")
print ("")
lista=lt.newList (datastructure='ARRAY_LIST')
lt.addFirst(lista,200)
lt.insertElement(lista,32,1)
lt.insertElement(lista,44,2)
lt.insertElement(lista,55,3)
lt.insertElement(lista,30,4)
lt.insertElement(lista,2,5)

shellSort(lista,lessfunction)
print ("Estamos haciendo una prueba de uso de la estructura de datos List de tipo Array list")
print (lista)