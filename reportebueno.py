# !/usr/bin/env python
# -*-conding:utf-8-*-

from tqdm import *
import os
import datetime
import time

fecharh = datetime.datetime.now().strftime("%d%m%y%H%M%S")
listaa = []
listab = []
sp = ";"

print "\n"
print "\n"
print "#############################################################"
print "##  SISTEMA DE REPORTE DE DIAJULIANO AAALAC - ISELAC v3.2  ##"
print "#############################################################"
print "\n"

diajul = raw_input("Que dia juliano inicial?")
print "\n"
diajulf = raw_input("Que dia juliano final?")
print "\n"
compacion = int(diajulf) - int(diajul)
if compacion < 0:
    print "Dia Juliano inicial debe ser mayor que le final \n"
else:
    print "Proceso Lectura de archivos espere por favor ... \n"
    for x in tqdm(range(int(compacion)+1)): #  Ciclo inical de los dias juliano
        diajul = str(diajul)
        g = diajul
        if len(g) == 1 or len(g) == 2: #  Relleno de ceros para cuando no son 1 a 2 digitos los dias juliano
            g = diajul.rjust(3, "0")
            diajul = g
        time.sleep(.01)
        # Ciclo de las cantidad de dias
        ciclo = str(datetime.date.today().year) 
        carpeta = "Concentra/Dia" + ciclo[2:4] + str(diajul) + "/Aduana51" #  carpeta dia juliano
        if os.path.isdir(carpeta): #  Ver si existe la carpeta
            # Verificacion de existencia de carpeta
            lista = os.listdir(carpeta) #  Lista de archivos
            for x in tqdm(xrange(1, len(lista), 1)): #  Ciclo de los archivos
                time.sleep(.01)
                # Ciclo de archivos ciclo para creacion de primera lista
                archivo = lista[x] #  Archivo
                if len(archivo) == 13: #  Para eleminar los nombre de archivos repetidos por medio de la Web
                    archivo = archivo[0:12]
                if archivo[0].upper() == "M":  # --> Archivos Pedimentos
                    leer = open(carpeta + "/" + archivo, "r+")
                    linea = leer.readline() #  Lee la linea
                    while linea != "": #  Barrido de linea
                        if linea[0:3] == "501": #  Registro General
                            patente = linea[4:8]
                            pedimento = linea[9:16]
                            to = linea[21:22]
                            cvd = linea[23:25]
                            rfc = linea[31:43]
                            pedg = patente + pedimento + to + cvd + rfc
                            listaa += [pedg]
                        linea = leer.readline()
                    leer.close()        
                elif archivo[0].upper() == "A": # --> Archivos Pago
                    leer = open(carpeta + "/" + archivo, "r+")
                    linea = leer.readline() #  Lee la linea
                    while linea != "": #  Barrido de linea
                        if linea[0:2] == "30": #  Registro General
                            paten = linea[4:8]
                            pedim = linea[8:15]
                            fecpgo = linea[50:58]
                            pedg = paten + pedim + fecpgo + archivo
                            listab += [pedg]
                        linea = leer.readline()
                    leer.close()        
        diajul = int(diajul) + 1
    # --------> Limpiado de lista A pedimentos pagados
    print "\n"
    print "Proceso de Depuracion espere por favor .... \n"
    for i in tqdm(range(len(listaa)-1, -1, -1)):
        time.sleep(.01)
        if listaa[i] in listaa[:i]:
            del(listaa[i])
    # --------> Limpiado de lista B pedimentos pagados
    for i in tqdm(range(len(listab)-1, -1, -1)):
        time.sleep(.01)
        if listab[i] in listab[:i]:
            del(listab[i])
    tempago = open("temporalpago" + fecharh + ".txt", "a")
    tempago.write(str(listab))
    tempago.close()
    # --------> Combinacion de listas
    print "\n"
    print "Proceso de Consolidacion espere por favor .... \n"
    for i in tqdm(range(len(listab)-1, -1, -1)):
        pedimentob = str(listab[i])[0:11]
        for x in tqdm(range(len(listaa)-1, -1, -1)):
            pedimentoa = str(listaa[x])[0:11]
            if pedimentob in pedimentoa:
                reporte = open("Reporte" + fecharh + ".txt", "a")
                patente = str(listaa[x])[0:4] + sp
                pedimento = str(listaa[x])[4:11] + sp
                tipooperacion = str(listaa[x])[11:12] + sp
                clavedoc = str(listaa[x])[12:14] + sp
                rfcc = str(listaa[x])[14:33] + sp
                fechapago = str(listab[i])[11:19] + sp
                archivopago = str(listab[i])[19:31] + sp
                lineafinal = patente + pedimento + tipooperacion + clavedoc + rfcc + fechapago + archivopago
                reporte.write(lineafinal + "\n")
                reporte.close()
    print "\n"
    print "Fin del archivo"





