# !/usr/bin/env python
# -*-conding:utf-8-*-

from tqdm import *
from PIL import Image
import os
import sys

print "\n"
print "\n"
print "####################################################"
print "##  SISTEMA COVERSION DE ARCHIVOS JPG A PDF v2.0  ##"
print "##                  XOYOC.NET                     ##"
print "####################################################"
print "\n"

directorio_inicial = os.getcwd() # Directorio Actual
contenido = os.listdir(directorio_inicial) # Contenido de la carpeta actual

print "Directorio Actual es --->" + directorio_inicial
print "Barra de proceso Inicial"

for dirName, subdirList, fileList in os.walk(directorio_inicial, topdown=False):
	print dirName
	for elemento in tqdm(fileList):
		elemento = dirName + os.sep + elemento
		if os.path.isfile(elemento): # condicional para saber si es un archivo
			archivo, extencion = os.path.splitext(elemento)
			if extencion == ".jpg" or extencion == ".JPG":
				filename = elemento
				try:
				    newfilename = os.path.splitext(filename)[0] + ".pdf"
				    Image.open(filename).save(newfilename)
				except IOError:
					print "Error al convertir archivo"
