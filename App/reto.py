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

import App.comparation as comp
from ADT import list as lt
from Sorting.shellsort import shellSort as sort
from DataStructures import listiterator as it
from DataStructures import liststructure as lt

from time import process_time 

def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Crear un ranking a partir de una lista de opciones")
    print("3- Conocer un director")
    print("4- Conocer un actor")
    print("5- Entender un genero")
    print("6- Crear ranking a partir de un genero")
    print("0- Salir")

def printRankingMenu() -> None:
    """
    Imprime las categorias para crear un ranking
    """
    print("\nCategorias:")
    print("1- Mas votada")
    print("2- Menos votada")
    print("3- Mejor puntuación")
    print("4- Peor puntuación")


def compareRecordIds (recordA, recordB):
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
        return 1
    return -1


def loadCSVFile (file, cmpfunction):
    t1_start = process_time()
    lst=lt.newList("ARRAY_LIST", cmpfunction)
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        with open(cf.data_dir + file, encoding="utf-8-sig") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for elemento in row: 
                lt.addLast(lst,elemento)
    except:
        print("Hubo un error con la carga del archivo")
        
    t1_stop = process_time()  #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst

def loadMoviesDetails ():
    lstmoviesdetails = loadCSVFile("themoviesdb/AllMoviesDetailsCleaned.csv",compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lstmoviesdetails)) + " elementos cargados")
    return lstmoviesdetails

def loadMoviesCasting ():
    lstmoviescasting = loadCSVFile("themoviesdb/AllMoviesCastingRaw.csv",compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lstmoviescasting)) + " elementos cargados")
    return lstmoviescasting

def conocer_director(lst1,lst2,name):
    ids=[]
    pelis=[]
    num=0
    vote=0
    t1_start = process_time()
    for a in lst1["elements"]:
        if name.lower() == a["director_name"].lower():
           num+=1
           ids.append(a["id"])
    for b in lst2["elements"]:
        i=0
        while i < len(ids):
            if b["id"]== ids[i]:
               vote+=float(b["vote_average"])
               pelis.append(b["title"])
            i+=1     
    prom=(vote/num)
    t1_stop = process_time()
    tiempo_total = t1_stop - t1_start
    print('El tiempo de ejecucion fue de', tiempo_total, 'segundos.')
    resul=(pelis,num,prom)
    return resul

def conocer_actor(lst1,lst2,name):
    ids=[]
    pelis=[]
    direct={}
    num=0
    vote=0
    t1_start = process_time()
    for a in lst1["elements"]:
        if (name.lower() == a["actor1_name"].lower()) or (name.lower() == a["actor2_name"].lower()) or (name.lower() == a["actor3_name"].lower()) or (name.lower() == a["actor4_name"].lower()) or (name.lower() == a["actor5_name"].lower()):
           num+=1
           ids.append(a["id"])
           if a["director_name"] not in direct:
              direct[a["director_name"]]=1
           else:
              direct[a["director_name"]]+=1     
    for b in lst2["elements"]:
        i=0
        while i < len(ids):
            if b["id"]== ids[i]:
               vote+=float(b["vote_average"])
               pelis.append(b["title"])
            i+=1     
    maydirect= max(direct.keys())
    prom=(vote/num)
    t1_stop = process_time()
    tiempo_total = t1_stop - t1_start
    print('El tiempo de ejecucion fue de', tiempo_total, 'segundos.')
    resul=(pelis,num,prom,maydirect)
    return resul          




def genre(lst, genero):
    lista_genero = []
    lista_votos = []
    t1_start = process_time()
    for pel in lst['elements']:
        if genero.lower() in pel['genres'].lower():
            lista_genero.append(pel['original_title'])
            lista_votos.append(int(pel['vote_count']))
    lista_todo = ['Ninguna', 0, 0]
    tiempo_total = 0
    votos_totales = 0       
    if (len(lista_votos))== 0: 
        print('No se encontro el genero')
    else:
        for votos in lista_votos:
            votos_totales+=votos
        promedio = votos_totales/(len(lista_votos))
        lista_todo = [lista_genero,len(lista_genero), promedio]
    t1_stop = process_time()
    tiempo_total = t1_stop - t1_start
    print('El tiempo de ejecucion fue de', tiempo_total, 'segundos.')
    return lista_todo

def orderElementsByCriteria(data,less):
    t1_start = process_time()
    sort(data, less)
    ranking = lt.newList("SINGLE_LINKED")
    for i in range(1,11):
        lt.addFirst(ranking,lt.getElement(data, i))

    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ", t1_stop - t1_start, " segundos")
    return ranking


def CrearRanking(data):
    categoria = (
        'vote_count',
        'vote_average'
    )
    switch = True
    while switch:
        printRankingMenu()
        criteria = int(input('Seleccione una opción para continuar\n'))
        if (criteria <= 4) and (criteria > 0):
            switch = False
        else:
            print("Opcion no valida")

    less = comp.Comparation(categoria[(criteria-1) // 2])
                
    t1_start = process_time()
    if criteria % 2 == 1:
        temp = orderElementsByCriteria(data,less.upVal)
    else:
        temp = orderElementsByCriteria(data, less.downVal)

    ranking = lt.newList("ARRAY_LIST")
    for i in range(1, lt.size(temp)):
        element = lt.getElement(temp,i)
        lt.addLast(ranking,(element["title"], element[categoria[(criteria-1) // 2]]))

    del temp
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución Total", t1_stop - t1_start, " segundos")
    return ranking
            
def printRanking(ranking):
    top = 1
    print('\n')
    for i in range(1, lt.size(ranking)):
        element = lt.getElement(ranking,i)
        print(f'{top}. {element[0]} con {element[1]}')
        top += 1

def getGenresList(data, genero):
    t1_start = process_time()
    lista = lt.newList('ARRAY_LIST')
    for i in range(1, lt.size(data)):
        element = lt.getElement(data, i)
        if element['genres'].lower() == genero.lower():
            lt.addLast(lista, element)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ", t1_stop - t1_start, " segundos")
    return lista
    
def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    data = False
    

    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        
        if len(inputs)>0 and (data or int(inputs[0])<=1):
            if int(inputs[0])==1: #opcion 1
                t1_start = process_time()
                lstmoviesdetails = loadMoviesDetails()
                lstmoviescasting = loadMoviesCasting()
                data = True
                t1_stop = process_time() #tiempo final
                print("Tiempo de ejecución Total: ", t1_stop - t1_start, " segundos")
            elif int(inputs[0])==2: #opcion 2
                ranking = CrearRanking(lstmoviesdetails)
                printRanking(ranking)
                del ranking

            elif int(inputs[0])==3: #opcion 3
                    name = input("Ingrese el director que quisiera conocer: ")
                    resul=conocer_director(lstmoviescasting,lstmoviesdetails,name)
                    print("Las películas que dirigió", name,"son:", resul[0]," ,en total son",resul[1],"peliculas, y el promedio de calificación es de",round(resul[2],2))
                            
            elif int(inputs[0])==4: #opcion 4
                    name = input("Ingrese el actor que quisiera conocer: ")
                    resul=conocer_actor(lstmoviescasting,lstmoviesdetails,name)
                    print("Las películas en las que estuvo", name,"son:", resul[0]," ,en total son",resul[1],"peliculas, el promedio de calificación es de",round(resul[2],2),"y el director con el que tiene más colaboraciones es",resul[3])

            elif int(inputs[0])==5: #opcion 5
                if lstmoviesdetails == None or lstmoviesdetails['size']==0:
                    print('Lista vacia')
                else:
                    genero = input('Ingrese el genero que desea conocer:')
                    lista_todo = genre(lstmoviesdetails, genero)
                    print('Las peliculas que pertencen al genero', genero, 'son', lista_todo[0], ',en total son', lista_todo[1], 'y el promedio de votos es', lista_todo[2])
        
            elif int(inputs[0])==6: #opcion 6
                genero = input('Ingrese el genero del que desea crear el ranking: ')
                listGenre = getGenresList(lstmoviesdetails, genero)
                ranking = CrearRanking(listGenre)
                printRanking(ranking)
                del ranking
                del listGenre


            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
        else:
            print("Porfavor, cargue datos")

if __name__ == "__main__":
    main()




    


    