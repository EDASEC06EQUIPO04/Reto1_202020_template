"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
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


import config as cf
from ADT import list as lt

def insertionSort (lst, lessfunction): 
    size =  lt.size(lst) 
    pos1 = 1
    while pos1 <= size:
        pos2 = pos1
        while (pos2 >1) and (lessfunction (lt.getElement(lst, pos2),lt.getElement(lst, pos2-1))):
            lt.exchange (lst, pos2, pos2-1)
            pos2 -= 1
        pos1 += 1

def insertionSortVoteCount (lst): 
    size =  lt.size(lst) 
    pos1 = 1
    while pos1 <= size:
        pos2 = pos1
        value1= (lt.getElement(lst, pos2))['vote_count']
        value2= (lt.getElement(lst, pos2-1))['vote_count']
        while (pos2 >1) and ( int(value1) ) < (int(value2) ):
            lt.exchange (lst, pos2, pos2-1)
            pos2 -= 1
        pos1 += 1


def insertionSort2 (lst, criterio, orden):
#criterio='vote_count'
    criterio=criterio

    if criterio=='vote_count':
    
        size =  len(lst)-1 
        pos1 = 1
    
        for index in range(1,len(lst)):
            currentvalue = int(lst[index][criterio])
            position = index
            original=lst[index]
      #print (currentvalue, " " , index , "  ", position)
      #input ("clic para avanzaar")
            while position>0 and int(lst [position-1][criterio])>int(currentvalue):
                lst [position]=lst [position-1]
                position = position-1
          #print (currentvalue)
            lst[position]=original

   

    if (orden == "less"):
            print ("Se ordeno Descendentemente")
            input ("Se finalizo el proceso...")
    if (orden=="greater"):
            #input ("estoy aqui")
            print ("Se ordeno ascendentemente")
            input ("Se finalizo el proceso...")

    if criterio=='vote_average':
   
        size =  len(lst)-1 
        pos1 = 1
    
        for indexe in range(1,len(lst)):
        #print (lst[indexe][criterio])    
            currentvalue = (lst[indexe][criterio])
            position = indexe
            original=lst[indexe]
            while (position>0 and (lst [position-1][criterio])>(currentvalue)):
                lst [position]=lst [position-1]
                position = position-1
                #print (currentvalue)
            lst[position]=original

    return lst

