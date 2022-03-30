#!/usr/bin/python
import re

def obtenerTexto(rutaArchivo):
    with open(rutaArchivo, 'r') as archivo:
        textoOriginal = archivo.read()
    return textoOriginal

def filtrarTexto(texto, palabras_prohibidas_path):
    nuevo_texto = texto
    palabras_prohibidas = obtenerTexto(palabras_prohibidas_path).split('\n')
    for palabra in palabras_prohibidas:
        nuevo_texto = (re.sub(rf'\b{palabra}\b', r' ', nuevo_texto))

    return nuevo_texto
