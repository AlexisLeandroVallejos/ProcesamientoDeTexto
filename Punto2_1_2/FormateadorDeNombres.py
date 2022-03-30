#!/usr/bin/python
import re


def procesar(str):
    registros = (re.split('/+', str))
    for registro in registros:
        datos = (re.split(',+', registro))
        print(datos[0] + " " + datos[1])
