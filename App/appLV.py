"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv
from ADT import list as lt
from DataStructures import listiterator as it
#from DataStructures import liststructure as lt
from Sorting.insertionsort import lessfunction
from time import process_time 
from Sorting import insertionsort  as InsSort
from Sorting import shellsort as shell
from Sorting import selectionsort as seSort

def loadCSVFileNew (file, sep=";")->list:
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None  
    """
    lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    #lst = lt.newList() #Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst


def loadCSVFile (file, lst, sep=";")->list:
    """
    Carga un archivo csv a una lista
    Args:
        file 
            Archivo de texto del cual se cargaran los datos requeridos.
        lst :: []
            Lista a la cual quedaran cargados los elementos despues de la lectura del archivo.
        sep :: str
            Separador escodigo para diferenciar a los distintos elementos dentro del archivo.
    Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None   
    """
    del lst[:]
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep

    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lst.append(row)
    except:
        del lst[:]
        print("Se presento un error en la carga del archivo")
    
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
     

    #for i in range (0,len(lst)-1,1):
    #    print (lst[i])
    input ("Ya se cargo el archivo, Clic para continuar")
    return lst


def printMenu():
    """
    Imprime el menu de opciones
    """
 
    print("\n**************************************************************************************")
    print("\n Bienvenidos a la consola del RETO 1           ***** EXPLORANDO LAMAGIA DEL CINE *****")
    print("\n**************************************************************************************")
    print ("CARGA DE DATOS")
    print("     (1)  Lab 0 - Cargar Datos de Archivos Large ")
    print("     (2)  Lab 0 - Cargar Datos de Archivos Small ")
    print("     (3)  Lab 0 - Cargar cualquier archivo por nombre")
    print ("")
    print ("REQUERIMIENTO 2 - Crear Ranking de peliculas")
    print("     (4)  Lab 2 - Ordenar por Vote Count Ascendente")
    print("     (5)  Lab 2 - Ordenar por Vote Count Descendente")
    print("     (6)  Lab 2 - Ordenar por Vote Average Ascendente")
    print("     (7)  Lab 2 - Ordenar por Vote Average Descendente")
    print("     (8)  Lab 2 - The Best Movies")
    print("     (9)  Lab 2 - The Worst Movies")
    print("     (10) Lab 2 - Shell sort")
    print("     (11) Lab 2 - Selection Sort")

    print ("")
    print ("REQUERIMIENTO 3 - Conocer un director")
    print("     (11) Lab 3 - Listar las peliculas de un director")
    print("     (12) Lab 3 - numero de peliculas del director")
    print("     (13) Lab 3 - promediode la calificacion de las peliculas del director")
    print ("")
    
    print("     0- Salir")

"""   De aqui en adelante  procedimientos para el Lab 0"""
    
def peliculasBuenas(lst1: list)-> int:
    #print(lst1)
    print("Aqui estoy ")
    nRegistros= len(lst1)
    pelBuenas=0
    for i in range (0, nRegistros, 1):
        if (float(lst1[i]['vote_average']) >= 6):
            pelBuenas+=1
            
        #print(lst1[i]['vote_average'])
        #pelBuenas=pelBuenas+ float(lst1[i]['vote_average'])
    #print(pelBuenas)    
    #input("Click para continuar")
   
    return pelBuenas

def PromedioPeliculasBuenas(lst1: list)-> float:
    #print(lst1)
    print("Aqui estoy ")
    nRegistros= len(lst1)
    pelBuenas=0
    proBuenas=0.0
    for i in range (0, nRegistros, 1):
        if (float(lst1[i]['vote_average']) >= 6):
            pelBuenas+=1
            proBuenas= proBuenas + float(lst1[i]['vote_average'])
        #print(lst1[i]['vote_average'])
        #pelBuenas=pelBuenas+ float(lst1[i]['vote_average'])
    #print(pelBuenas)    
    #input("Click para continuar")
    proBuenas=proBuenas/pelBuenas
    return proBuenas

def peliculasBuenasDirector(lst1: list, lst2:list,  director:str)-> None:
    #print(lst1)
    print("Aqui estoy ")
    nRegistros= len(lst1)
    pelBuenasDirector=0
    proBuenas=0.0
    NuPeliculas=0
    for i in range (0, nRegistros, 1):
        if ( lst2[i]['director_name'] == director):
            NuPeliculas= NuPeliculas+1
        if (float(lst1[i]['vote_average']) >= 6) and (lst2[i]['director_name'] == director):
            pelBuenasDirector+=1
            proBuenas= proBuenas + float(lst1[i]['vote_average'])
            
        #print(lst1[i]['vote_average'])
        #pelBuenas=pelBuenas+ float(lst1[i]['vote_average'])
    #print(pelBuenas)    
    #input("Click para continuar")
    if pelBuenasDirector != 0:
        proBuenas= proBuenas/pelBuenasDirector
        respuesta=(pelBuenasDirector, proBuenas)
    print("El numero de peliculas del director " , director , " son: ", NuPeliculas ,"de las cuales ", pelBuenasDirector, "son buenas. Con un promedio de: ", round(proBuenas,2)) 
    input ("Clic para cotinuar")
  #  return respuesta

    """   De aqui en adelante debemos desarrollar los procedimientos para el Lab 1"""
  

def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if lst['size']==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        iterator = it.newIterator(lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1           
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(criteria, column, lst):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    return 0

def orderElementsByCriteria(function, column, lst, elements):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    return 0

def iSort (lst:list, criterio:str, orden:str)->list: 
    t1_start = process_time() #tiempo inicial
    input ("Vamos a proceder a ordenar usando el metodo Insertion Sort, esto puede tomar algunos segundos o minutos. Clic para continuar")
    listaOrdenada = []
    listaOrdenada=InsSort.insertionSort (lst,criterio, orden)
    t1_stop = process_time() #tiempo final
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Tiempo de ejecución de metodo InsertionSort ",t1_stop-t1_start," segundos")
    input ("Dar clic para continuar...")
    return listaOrdenada

def buscarMovies (lista2:list,cantidad:int)->None:
     
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++  The Best Movies +++++++++++++++++++++++++++++++++")
    for i in range (0,cantidad,1):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(lista2[i],"\n")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    input ("Dar clic para continuar...")

def buscarMoviesWorst (lista2:list,cantidad:int)->None:
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++  The Best Movies +++++++++++++++++++++++++++++++++")
    for i in range (len(lista2)-1,len(lista2)-12-cantidad,-1):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(lista2[i],"\n")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    input ("Dar clic para continuar...")

def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista1 = []  # se require usar lista definida peliculas
    lista2 = []  # se require usar lista definida directores casting
    lista3 = []   # se require usar lista definida books
    """
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                lista = loadCSVFile("Data/test.csv") #llamar funcion cargar datos
                print("Datos cargados, ",lista['size']," elementos cargados")

            elif int(inputs[0])==2: #opcion 2
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    

                else: print("La lista tiene ",lista['size']," elementos")

            elif int(inputs[0])==3: #opcion 3
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:   
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsFilteredByColumn(criteria, "nombre", lista) #filtrar una columna por criterio  
                    print("Coinciden ",counter," elementos con el crtierio: ", criteria  )

            elif int(inputs[0])==4: #opcion 4
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsByCriteria(criteria,0,lista)
                    print("Coinciden ",counter," elementos con el crtierio: '", criteria ,"' (en construcción ...)")
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
        """    
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar:  ') #leer opción ingresada
        print ("Usted selecciono: ", inputs)
        if len(inputs)>0:
            if int(inputs)==1: #opcion 1
                lista1=loadCSVFile("Data/theMoviesdb/MoviesDetailsCleaned-large.csv", lista1) 
                print("Datos cargados de Movies Large, ",len(lista1)," elementos cargados")
                lista2=loadCSVFile("Data/theMoviesdb/MoviesCastingRaw-large.csv", lista2 ) 
                print("Datos cargados de Casting Large, ",len(lista2)," elementos cargados")
                input ("Clic para cotinuar...")

            elif int(inputs)==2: #opcion 2
                lista1=loadCSVFile("Data/theMoviesdb/MoviesDetailsCleaned-small.csv", lista1) 
                print("Datos cargados de Movies Small, ",len(lista1)," elementos cargados")
                lista2=loadCSVFile("Data/theMoviesdb/MoviesCastingRaw-small.csv", lista2) 
                print("Datos cargados de Casting Small, ",len(lista2)," elementos cargados")
                input ("Clic para cotinuar")
            
            elif int(inputs)==3: #opcion 3
                
                input ("Clic para continuar")
                fileToLoad = input ("Digite el nombre del archivo [ ejemplo: Data/GoodReads/books.csv ] : ")
                lista1=loadCSVFile(fileToLoad) 
                print("Datos cargados del archivo [",fileToLoad, " ]: ", len(lista1))
                
                input ("Clic para cotinuar")

            elif int(inputs)==4: #opcion 4
                 orden="less"
                 criterio='vote_count'
                 #print (lista1)
                 #input ("Clic para avanzar")
                 lista3=iSort (lista1,criterio, orden)
                 print  ("Se ha ordenado la lista")

            elif int(inputs)==5: #opcion 5
                 orden="greater"
                 criterio='vote_count'
                 #print (lista1)
                 #input ("Clic para avanzar")
                 lista3=iSort (lista1,criterio, orden)
                 print  ("Se ha ordenado la lista")
            elif int(inputs)==6: #opcion 6
                 orden="less"
                 criterio='vote_average'
                 #print (lista1)
                 #input ("Clic para avanzar")
                 lista3=iSort (lista1,criterio, orden)
                 print  ("Se ha ordenado la lista")
            elif int(inputs)==7: #opcion 7 
                 orden="greater"
                 criterio='vote_average'
                 #print (lista1)
                 #input ("Clic para avanzar")
                 lista3=iSort (lista1,criterio, orden)
                 print  ("Se ha ordenado la lista")               
                 input ("En construccion....Clic para cotinuar")

            elif int(inputs)==8: #opcion 8
                cantidad=int(input ("Digite el numero de pelicuales que dea lisar:"))
                buscarMovies (lista1,cantidad)
                input ("En construccion....Clic para cotinuar")

            elif int(inputs)==9: #opcion 9
                cantidad=int(input ("Digite el numero de pelicuales que dea lisar:"))
                buscarMoviesWorst (lista1,cantidad)
                input ("En construccion....Clic para cotinuar")

            elif int(inputs)==10: #opcion 10
                lista1=lt.newList (datastructure='ARRAY_LIST')   
                #lista1=lt.newList (datastructure='SINGLE_LINKED') 
                #lista1 = lt.newList() 
                lista1=loadCSVFileNew("Data/theMoviesdb/MoviesDetailsCleaned-small.csv") 
                shell.shellSort(lista1,lessfunction)
                
                input ("Se ordenaron ascendentemente las peliculas por el campo  ** Vote Count ** ....Clic para cotinuar")
            elif int(inputs)==11: #opcion 11
                
                lista1=lt.newList ()
                #lista1=lt.newList (datastructure='ARRAY_LIST')   
                #lista1=lt.newList (datastructure='SINGLE_LINKED') 
                #lista1 = lt.newList() 
                lista1=loadCSVFileNew("Data/theMoviesdb/MoviesDetailsCleaned-small.csv") 
                seSort.selectionSort(lista1,lessfunction)         

            elif int(inputs)==12: #opcion 12
                input ("En construccion....Clic para cotinuar")           
            elif int(inputs)==13: #opcion 13
                input ("En construccion....Clic para cotinuar")           
            
            elif int(inputs)==0: #opcion 0, salir
                sys.exit(0)  

            
                
if __name__ == "__main__":
    main()