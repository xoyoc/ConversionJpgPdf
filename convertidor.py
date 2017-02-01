# !/usr/bin/env python
# -*-conding:utf-8-*-

from tqdm import *
from PIL import Image
import os
import sys

print "\n"
print "\n"
print "####################################################"
print "##  SISTEMA COVERSION DE ARCHIVOS JPG A PDF v2.1  ##"
print "##                  XOYOC.NET                     ##"
print "####################################################"
print "\n"

directorio_inicial = os.getcwd() # Directorio Actual
contenido = os.listdir(directorio_inicial) # Contenido de la carpeta actual

print "Directorio Actual es --->" + directorio_inicial
print "Barra de proceso"

for dirName, subdirList, fileList in os.walk(directorio_inicial, topdown=False): # Barra de barrido de directorios
	print dirName # Directorio de scaneo para la conversion
	for elemento in tqdm(fileList):
		elemento = dirName + os.sep + elemento
		if os.path.isfile(elemento): # condicional para saber si es un archivo
			archivo, extencion = os.path.splitext(elemento)
			if extencion == ".jpg" or extencion == ".JPG":
				filename = elemento
				try:
				    newfilename = os.path.splitext(filename)[0] + ".pdf"
				    Image.open(filename).save(newfilename)
				    os.remove(elemento)
				except IOError:
					print "Error al convertir archivo"
