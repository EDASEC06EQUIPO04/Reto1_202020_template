import config as cf
import sys
import csv
import unicodedata
import re


from ADT import list as lt
from DataStructures import listiterator as it

from Sorting import insertionsort as insertion


#from Sorting.insertionsort import lessfunction
from Sorting import insertionsort  as InsSort
from Sorting import shellsort as shell
from Sorting import selectionsort as seSort
from time import process_time 
from itertools import chain
from operator import itemgetter



def printMenu():


    print ("CARGA DE DATOS")
    print("     (1)  Cargar archivos ")
    print("")
    print ("REQUERIMIENTO 1 - Crear Ranking de peliculas")
    print("     (2)  Consultar buenas peliculas")
    print("")
    print ("REQUERIMIENTO 2 - Crear Ranking de peliculas")
    print("     (3)  Ordenar por Vote Count Ascendente")
    print("")
    print ("REQUERIMIENTO 3 - Conocer un director")
    print("     (4) Información sobre el trabajo de un director")
    print("")
    print ("REQUERIMIENTO 4 - Información de un actor")
    print("     (5) Información sobre el trabajo de un director")  
    print("")
    print ("REQUERIMIENTO 5 - Entender un género cinematográfico")
    print("     (6) películas asociadas al género") 
    print("")
    print ("REQUERIMIENTO 6 - Crear ranking del género")
    print("     (7) ranking de genero ")
    print("")
    print("     0- Salir")

    print("\n**************************************************************************************")
    print("\n Bienvenidos a la consola del RETO 1           ***** EXPLORANDO LAMAGIA DEL CINE *****")
    print("\n**************************************************************************************")
    print ("CARGA DE DATOS")
    print("     (1)  Cargar Datos de Archivos Large ")
    print("     (2)  Cargar Datos de Archivos Small ")
    print("     (3)  Cargar cualquier archivo por nombre")
    print ("")
    print ("REQUERIMIENTO 1 - Crear Ranking de peliculas")
    print("     (4)  Consultar numero de peliculas buenas (vote_average>=6)")
    print("     (5)  Cacular el promedio de la votacion")
    print("     (6)  Consultar buenas peliculas por director")
    print ("")
    print ("REQUERIMIENTO 2 - Crear Ranking de peliculas")
    print("     (7)  Ordenar por Vote Count Ascendente")
    print("     (8)  Ordenar por Vote Count Descendente")
    print("     (9)  Ordenar por Vote Average Ascendente")
    print("     (10) Ordenar por Vote Average Descendente")
    print("     (11) The Best Movies")
    print("     (12) The Worst Movies")
    # print("     (13) Shell sort")
    #print("     (14) Selection Sort")

    print ("")
    print ("REQUERIMIENTO 3 - Conocer un director")
    print("     (15) Listar las peliculas de un director")
    print("     (16) Numero de peliculas del director")
    print("     (17) Promedio de la calificacion de las peliculas del director")
    print ("")

    print ("REQUERIMIENTO 4 - Información de un actor")
    print("     (18) Listar las peliculas de un actor")
    print("     (19) numero de peliculas en las que ha participado")
    print("     (20) Nombre del director con el que mas colaboraciones ha tenido")
    print("     (21) Cantidad de películas en las que ha participado")    
    print ("") 
    print ("REQUERIMIENTO 5 - Entender un género cinematográfico")
    print("     (22) lista de todas las películas asociadas al género")
    print("     (23) La cantidad de películas encontradas")
    print("     (24) El promedio de votos (vote_count) del género")  
    print ("") 
    print ("REQUERIMIENTO 6 - Crear ranking del género")
    print("     (25) Lista de las películas que hacen parte del ranking ")
    print("     (26) El promedio de votos y calificación (vote_count) películas que hacen parte del ranking.")
    print("     (27) El promedio de votos y calificación (vote_average) dpelículas que hacen parte del ranking.")  
    print ("") 
    print("     0- Salir")

"""   De aqui en adelante  procedimientos para el Lab 0"""



def compareRecordIds (recordA, recordB):
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
        return 1
    return -1




def loadCSVFile (file,cmpfunction):
    sep=";"
    #lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    lst = lt.newList("SINGLE_LINKED") #Usando implementacion linkedlist
    

    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    
    return lst



def loadMoviesDetails ():
    lst = loadCSVFile("Data/themoviesdb/SmallMoviesDetailsCleaned.csv",compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst


def loadMoviesCasting ():
    lst = loadCSVFile("Data/themoviesdb/MoviesCastingRaw-small.csv",compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst


def normalizeCase(caseInput:str):
    return caseInput.title()
    






#Metodo alternativo de load file implementado para coincidir con los parametros construidos en el metodo del req 2
def loadCSVFile1 (file, lst, sep=";")->list:


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
    return lst












"""
-----------------------------------REQUERIMIENTO 1-----------------------------------------
"""
#Input  nombre director 

#output1   lista de peliculas  
# output2   el promedio de calificaciones 
# output3   cantidad de peliculas ditrigidas


def EncontrarPeliculasBuenasDirector(lst1, lst2, nom_director):
    pelBuenas=0
    proBuenas=0.0
    for i in range (1, lt.size(lst1)):
        if (float(lt.getElement(lst1,i)['vote_average']) >= 6) and lt.getElement(lst2,i)['director_name']==normalizeCase(nom_director):
            pelBuenas+=1
            proBuenas= proBuenas + float(lt.getElement(lst1,i)['vote_average'])
    proBuenas=proBuenas/pelBuenas
    print("El numero de peliculas buenas del director son: ", pelBuenas)
    print("El promedio de las peliculas buenas del director son: ", round(proBuenas, 2))
    input ("presione una tecla para volver al menu...")

"""
-----------------------------------REQUERIMIENTO 2-----------------------------------------
"""
#input elegir al menos 10  peliculas
#output ordenar por vote count
#output ordenar por calificacion promedio
#output descendente o ascendente

def crearRankingPeliculas(lst, amount):


    peliculasSeleccionadas=[]
    
    for i in range(0, amount):
        peliculasSeleccionadas.append(lst[i])


    printMenuSortingcriteria()
    criteriaInput=str(input ("Ingrese el criterio para el ranking:\n"))
    if int (criteriaInput)==1: 
        criterio = 'vote_count'
    elif int(criteriaInput)==2: 
        criterio='vote_average'



    printMenuSortingOrder()
    orderInput=str(input ("seleccione el orden para el ranking\n"))
    if int (orderInput)==1: 
        orden = "less"
    elif int(orderInput)==2: 
        orden="greater"

    listaResults= insertion.insertionSort2(peliculasSeleccionadas,criterio,orden)

    for n in range(len(listaResults)):
            print((n+1, listaResults[n]['original_title'], listaResults[n][criterio]))
    input ("presione una tecla para volver al menu...")
















"""
-----------------------------------REQUERIMIENTO 3-----------------------------------------
"""

def ConocerTrabajoDirector (lista1, lista2, nom):
    #variables
    listaPelis=[]
    numpeliculas=0
    proPeliculas=0.0
#loop
    for x in range(0, lt.size(lista1)):
        y=lt.getElement(lista2, x)
        if (y["director_name"] == normalizeCase(nom)): 
            listaPelis.append(lt.getElement(lista1, x)["original_title"])
            numpeliculas += 1 
            proPeliculas = float(lt.getElement(lista1, x)['vote_average'])

    if numpeliculas != 0:

        promfinal= proPeliculas/numpeliculas
        print("La lista de peliculas es: ", listaPelis)
        print("El numero de peliculas dirigidas por el director es: ", numpeliculas)
        print("El promedio de la calificacion de las peliculas es: ", promfinal)

    else:

        print("Ha ocurrido un error, porfavor escriba el nombre de otro director")
    input ("presione una tecla para volver al menu...")

"""
----------------------------REQUERIMIENTO 4---------------------------------------------------------------------
"""

#Req 4
def ConocerTrabajoActor (lista1, lista2, nom):
    listaPelis=[]
    numpeliculas=0
    proPeliculas=0.0
    posiblesDirectores={}
    
    for x in range(1,  lt.size(lista1)):
        if ((lt.getElement(lista2, x)['actor1_name']) == normalizeCase(nom) or (lt.getElement(lista2, x)['actor2_name']) == normalizeCase(nom) or (lt.getElement(lista2, x)['actor3_name']) == normalizeCase (nom) or (lt.getElement(lista2, x)['actor4_name']) == normalizeCase (nom) or (lt.getElement(lista2, x)['actor5_name']) == normalizeCase (nom)):
            listaPelis.append(lt.getElement(lista1, x)['original_title'])
            numpeliculas += 1
            proPeliculas += float(lt.getElement(lista1, x)['vote_average'])

            nom_direc=lt.getElement(lista2, x)['director_name']
            if nom_direc in posiblesDirectores:
                posiblesDirectores[nom_direc] += 1
            else:
                posiblesDirectores[nom_direc] = 1

    
    if numpeliculas != 0:
        director=""
        i=0
        for x in posiblesDirectores:
            if posiblesDirectores[x] > i:
                i=posiblesDirectores[x]
                director = x

        promfinal= proPeliculas/numpeliculas
        print("La lista de peliculas es: ", listaPelis)
        print("El numero de peliculas en las que el actor ha partisipado son: ", numpeliculas)
        print("El promedio de la calificacion de las peliculas es: ", promfinal)
        print("El nombre del director con el que actor ha trabajado mas veces es: ", director)
    else:
        print("Ha ocurrido un error, porfavor escriba el nombre de otro actor")
    input ("presione una tecla para volver al menu...")



"""
-------------------REQUERIMIENTO 5-----------------------------------------------
"""

def buscarGeneroADT(list1, generoBuscado:str):
    resultList= lt.newList()
    averageVotes=0
    currentNumVotes=0
    totalVotes=0


#este loop recorre el array importado del csv  y crea un array nuevo con el contenido que cumple el criterio
    for i in range (0, lt.size(list1)):
        if (lt.getElement(list1, i)['genres'] in normalizeCase(generoBuscado)): #case insensitive
            lt.addLast(resultList, (lt.getElement(list1, i)))   #se agrega a la lista resultado
            currentNumVotes = int(lt.getElement(list1, i)['vote_count'])
            totalVotes= totalVotes + currentNumVotes    
    averageVotes=totalVotes/lt.size(resultList)#calculo del promedio de votos


    print ("Las peliculas encontradas son:" )
    for j in range (lt.size(resultList)):               #loop para imprimir todos los titulos encontrados con un indice
        print((j, (lt.getElement(resultList,j))['original_title']))
    print ("se encontraron" , lt.size(resultList) , "del genero especificado \nEl promedio de votos para el genero es ", averageVotes)
    input ("presione una tecla para volver al menu...")


"""
--------------------------REQUERIMIENTO 6 ----------------------------------------
"""
# input:elegir al menos 10 peliculas
#input:ranking ascendento o descendente
#inputordenar por vote count o  average

#out:lista de peliculas que hacen pare del ranking
#out: vote count y vote average de las peliculas que hace parte del ranking


def rankingPorGenero (list1, generoBuscado:str):

#generate list by given genre
    resultList2= lt.newList()
    averageVotes=0
    currentNumVotes=0
    totalVotes=0


#este loop recorre el array importado del csv  y crea un array nuevo con el contenido que cumple el criterio
    for i in range (0, lt.size(list1)):
        if (lt.getElement(list1, i)['genres'] in normalizeCase(generoBuscado)): #case insensitive
            lt.addLast(resultList2, (lt.getElement(list1, i)))   #se agrega a la lista resultado

    print ("Las peliculas encontradas son:" )
    for j in range (lt.size(resultList2)):               #loop para imprimir todos los titulos encontrados con un indice
        print((j, (lt.getElement(resultList2,j))['original_title'])) 
    print ("se encontraron" , lt.size(resultList2) , "del genero especificado \n")

#ask for input selection
    print ("Ingrese su selección de peliculas para el ranking\n puede ingresar numeros (1,2,3) o rangos(1-3)\n separados con una coma")
    rankingSearchInput=str(input ("Ingrese las peliculas escogidas:\n"))

#turn selection String into number array
    searchParameters= numberStringtoList(rankingSearchInput)
#create new array with given indexes
#no se utiliza el metodo lt.sublist pues este no incluye intervalos
    

    
    rankingList= lt.newList()

    
    for n in range (len(searchParameters)):    
        lt.addLast(rankingList, (lt.getElement(resultList2,n)))
        #rankingList.append(resultList[searchParameters[n]])
    
    for o in range(lt.size(rankingList)):
        print(o+1, (lt.getElement(resultList2,o))['original_title'])
    print('Se seleccionaron ', lt.size(rankingList), ' peliculas')

#ask for sorting criteria1
    printMenuSortingcriteria()
    criteriaInput=str(input ("Ingrese el criterio para el ranking:\n"))
    

#ask for sorting order
    if int (criteriaInput)==1: #vote count
        searchCriteria = 'vote_count'
    elif int(criteriaInput)==2: #vote average
        searchCriteria='vote_average'


    #ask for sorting
    printMenuSortingOrder()
    orderInput=str(input ("seleccione el orden para el ranking\n"))

    if int (orderInput)==1: #descendente
        #orderedRankingList= rankingList
        orderedRankingList= lt.newList()
        orderedRankingList=insertion.insertionSortVoteCount (rankingList)
        for n in range(lt.size(orderedRankingList)):
            print((n+1, orderedRankingList[n]['original_title'], orderedRankingList[n]['vote_count']))

    elif int(orderInput)==2: #vote average
        searchCriteria='vote_average'#ascendente







def printMenuSortingcriteria():
    print ("")
    print("     (1)   Ordenar por vote count")
    print("     (2)   Ordenar por vote average ")

def printMenuSortingOrder():
    print ("")
    print("   (1)   Orden descendente ")
    print("   (2)   Orden ascendente ")


# metodo basdo en https://stackoverflow.com/questions/6405208/how-to-convert-numeric-string-ranges-to-a-list-in-python
def numberStringtoList (inputNumbers:str):
    result= sum(((list(range(*[int(j) + k for k,j in enumerate(i.split('-'))]))
        if '-' in i else [int(i)]) for i in inputNumbers.split(',')), [])
    print(result)
    return result
























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
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar ?  ') #leer opción ingresada
        print ("Usted selecciono: ", inputs)
        if len(inputs)>0:
            if int(inputs)==1: #opcion 1
                lista1=loadCSVFile1("Data/theMoviesdb/MoviesDetailsCleaned-large.csv", lista1) 
                print("Datos cargados de Movies Large, ",len(lista1)," elementos cargados")
                lista2=loadCSVFile1("Data/theMoviesdb/MoviesCastingRaw-large.csv", lista2 ) 
                print("Datos cargados de Casting Large, ",len(lista2)," elementos cargados")
                input ("Clic para cotinuar...")


            if int(inputs[0])==1: #opcion 1
                lstmovies = loadMoviesDetails()  #lista1
                lstmovcas = loadMoviesCasting()  #lista2 
                print("datos cargados")

            elif int(inputs[0])==2: #opcion 2           REQ1
                director=str(input ("Ingrese el director a buscar:\n"))
                EncontrarPeliculasBuenasDirector(lstmovies, lstmovcas, director)

            elif int(inputs[0])==3: #opcion 3           REQ 2
                lista1=[]
                lista1=loadCSVFile1("Data/theMoviesdb/SmallMoviesDetailsCleaned.csv", lista1) 
                print("Datos cargados de Movies Small, ",len(lista1)," elementos cargados")
                numero=int(input ("Ingrese la cantidad de peliculas para crear ranking:\n"))
                crearRankingPeliculas(lista1, numero)
            elif int(inputs[0])==4: #opcion 4          REQU 3
                director=str(input ("Ingrese el director a buscar:\n"))
                ConocerTrabajoDirector(lstmovies, lstmovcas, director)


            elif int(inputs[0])==5: #opcion 5           REQU 4
                nomActor=str(input("Ingrese el; nombre de un actor"))
                ConocerTrabajoActor(lstmovies, lstmovcas, nomActor)
                
            elif int(inputs)==6: #opcion 6              REQ 5
                genero=str(input ("Ingrese el genero a buscar:\n"))
                buscarGeneroADT(lstmovies, genero)

            elif int(inputs[0])==7: #opcion 7        REQ 6 
                genero=str(input ("Ingrese el genero a buscar:\n"))
                rankingPorGenero(lstmovies, genero)


               input (" Estamos en constuccion.....Clic para cotinuar")         
            
            elif int(inputs)==0: #opcion 0, salir
                sys.exit(0)  

                
if __name__ == "__main__":
    main()
