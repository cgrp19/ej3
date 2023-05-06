import csv
import os
from Registro import Registro

class manejadorVM:
    __filas: int
    __columna: int
    __listaVM = []

    def __init__(self, filas=30, columna=24):
        self.__filas = filas
        self.__columna = columna

    def mostrarDatos(self):
        for i in range (len(self.__listaVM)):
            for j in range (len(self.__listaVM[i])):
                print (self.__listaVM[i][j].getPresion())

    def cargarDatos (self):
        for i in range (30):
            lista=[]
            for j in range (24):
                lista.append(0)
            self.__listaVM.append(lista)
        bandera = True
        path = './Variables_Meteorologicas.csv'
        archivo = open(path, 'r')
        reader = csv.reader(archivo, delimiter =',')
        for fila in reader:
            dia = int(fila[0]) ## filas, indice i
            hora = int(fila[1]) ## columnas, indice j
            temp = int(fila[2])
            hum = int(fila[3])
            pre = int(fila[4])
            xRegistro = Registro(temp, hum, pre)
            self.__listaVM[dia-1][hora] = xRegistro    
        print('Carga Lista!')
        os.system('pause')

    def mostrarMayoryMenor (self):
        os.system('cls')
        maxt = 0
        maxh = 0
        maxp = 0
        mint = 9999
        minh = 9999
        minp = 9999
        xi = 0 ## indice i para buscar
        xj = 0 ## indice j para buscar
        print ('---> VALORES MAXIMOS <---')
        for i in range (len (self.__listaVM)):
            for j in range (len (self.__listaVM[i])):
                if (self.__listaVM[i][j].getTemperatura() > maxt):
                    maxt = self.__listaVM[i][j].getTemperatura()
                    xi = i+1
                    xj = j
        print (f'->La temperatura máxima es {maxt}. Del día: {xi} a la hora: {xj}')
        for i in range (len (self.__listaVM)):
            for j in range (len (self.__listaVM[i])):
                if (self.__listaVM[i][j].getHumedad() > maxh):
                    maxh = self.__listaVM[i][j].getHumedad()
                    xi = i+1
                    xj = j
        print (f'->La humedad máxima es {maxh}. Del día: {xi} a la hora: {xj}')
        for i in range (len (self.__listaVM)):
            for j in range (len (self.__listaVM[i])):
                if (self.__listaVM[i][j].getPresion() > maxp):
                    maxp = self.__listaVM[i][j].getPresion()
                    xi = i+1
                    xj = j
        print (f'->La presion máxima es {maxp}. Del día: {xi} a la hora: {xj}')
        print ('''
---> VALORES MINIMOS <---
        ''')
        for i in range (len (self.__listaVM)):
            for j in range (len (self.__listaVM[i])):
                if (self.__listaVM[i][j].getTemperatura() < mint):
                    mint = self.__listaVM[i][j].getTemperatura()
                    xi = i+1
                    xj = j
        print (f'->La temperatura minima es {mint}. Del día: {xi} a la hora: {xj}')
        for i in range (len (self.__listaVM)):
            for j in range (len (self.__listaVM[i])):
                if (self.__listaVM[i][j].getHumedad() < minh):
                    minh = self.__listaVM[i][j].getHumedad()
                    xi = i+1
                    xj = j
        print (f'->La humedad minima es {mint}. Del día: {xi} a la hora: {xj}')
        for i in range (len (self.__listaVM)):
            for j in range (len (self.__listaVM[i])):
                if (self.__listaVM[i][j].getPresion() < minp):
                    minp = self.__listaVM[i][j].getPresion()
                    xi = i+1
                    xj = j
        print (f'->La presion minima es {mint}. Del día: {xi} a la hora: {xj}')

    def calcularPromedioMes (self):
        aux = 0
        cont = 0
        for i in range (len(self.__listaVM)):
            for j in range (len (self.__listaVM[i])):
                aux += int (self.__listaVM[i][j].getTemperatura())
                cont += 1
        return float (aux / cont)
    
    def listarPorDia (self, dia):  ## dia == indice i
        print ('______________________________________________')
        print ('|{:^10} {:^10} {:^10} {:^10}|'. format('Hora', 'Temperatura', 'Humedad', 'Presion'))
        print ('|--------------------------------------------|')
        for j in range (len (self.__listaVM[dia])):
            print ('|{:^10} {:^10} {:^10} {:^10} |'. format(j, self.__listaVM[dia][j].getTemperatura(), self.__listaVM[dia][j].getHumedad(), self.__listaVM[dia][j].getPresion()))
        print ('|____________________________________________|\n')