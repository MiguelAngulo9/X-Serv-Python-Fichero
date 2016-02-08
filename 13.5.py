#!/usr/bin/python
# -*- coding: utf-8 -*-

fich = open("/etc/passwd", "r");

lineas = fich.readlines()
diccionario = {}

for linea in lineas:
	elemento = linea.split(':')
	usuario = elemento[0]
	shell = elemento[-1]
	diccionario[usuario] = shell 


print "La shell de root es:", diccionario["root"]

try: 
	print diccionario["imaginario"]
except:
	print 'El nombre de usuario "imaginario" no existe. '
