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
from DataStructures import liststructure as lt

from time import process_time 



def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Ranking de peliculas")
    print("3- Conocer un director")
    print("4- Conocer un actor")
    print("5- Entender un genero")
    print("6- Crear ranking")
    print("0- Salir")




def compareRecordIds (recordA, recordB):
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
        return 1
    return -1


def loadCSVFile (file, cmpfunction):
    lst=lt.newList("ARRAY_LIST", cmpfunction)
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        with open(  cf.data_dir + file, encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for elemento in row: 
                lt.addLast(lst,elemento)
    except:
        print("Hubo un error con la carga del archivo")
    return lst

def loadMoviesDetails ():
    lstmoviesdetails = loadCSVFile("theMoviesdb/SmallMoviesDetailsCleaned.csv",compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lstmoviesdetails)) + " elementos cargados")
    return lstmoviesdetails

def loadMoviesCasting ():
    lstmoviescasting = loadCSVFile("theMoviesdb/Casting.csv",compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lstmoviescasting)) + " elementos cargados")
    return lstmoviescasting

def conocer_a_un_director(lstmoviescasting:list, lstmoviesdetails:list, d_name:str)->tuple:
    pelis=[]
    num=0
    vote=0
    i=0
    while i < len(lstmoviescasting):
        if lstmoviescasting[i]["director_name"]==d_name:
           num+=1
           prom+=lstmoviesdetails[i]["vote_average"]
           pelis.append(lstmoviesdetails[i]["title"])
        i+=1
    prom=(vote/num)
    return (pelis, num, prom)

def ejecutar_conocer_a_un_director(lstmoviescasting:list, lstmoviesdetails:list)->None:
    d_name = input("Ingrese el nombre del director que quiere conocer: ")
    x=conocer_a_un_director(lstcasting,lstdetails,d_name)
    print(x)          




def genre(lst, genero):
    lista_genero = []
    lista_votos = []
    t1_start = process_time()
    for pel in lst['elements']:
        if genero.lower() in pel['genres'].lower():
            lista_genero.append(pel['original_title'])
            lista_votos.append(int(pel['vote_count']))
    votos_totales = 0
    for votos in lista_votos:
        votos_totales+=votos
    
    promedio = votos_totales/(len(lista_votos))
    lista_todo = [lista_genero,len(lista_genero), promedio]
    t1_stop = process_time
    print('El tiempo de ejecucion fue de', t1_stop-t1_start, 'segundos')
    return lista_todo


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """


    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:

            if int(inputs[0])==1: #opcion 1
                lstmoviesdetails = loadMoviesDetails()
                lstmoviescasting = loadMoviesCasting()
            elif int(inputs[0])==2: #opcion 2
                pass

            elif int(inputs[0])==3: #opcion 3
                ejecutar_conocer_a_un_director(lstmoviecasting,lstmoviesdetails)

            elif int(inputs[0])==4: #opcion 4
                pass

            elif int(inputs[0])==5: #opcion 5
                if lstmoviesdetails == None or lstmoviesdetails['size']==0:
                    print('Lista vacia')
                else:
                    genero = input('Ingrese el genero que desea conocer:')
                    lista_todo = genre(lstmoviesdetails, genero)
                    print('Las peliculas que pertencen al genero', genero, 'son', lista_todo[0], ',en total son', lista_todo[1], 'y el promedio de votos es', lista_todo[2])
        
            elif int(inputs[0])==46: #opcion 6
                pass


            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()




    