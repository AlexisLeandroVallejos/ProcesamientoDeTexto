import re
from collections import Counter

LAS_PRIMERAS_CINCO = 5
regexSignosDePuntuacion = r'[.,;:"\\\'()\[\]{}?¿!¡—-]'
regexReemplazo = r' '
regexPalabra = r'\w+'

def abrirYLeerArchivo(rutaArchivo):
    with open(rutaArchivo, 'r') as archivo:
        textoOriginal = archivo.readlines()
    return textoOriginal

def solamenteMinusculas(texto):
    for linea in texto:
        linea.lower()
    return texto

def purgadorDeSignosDePuntuacion(texto):
    for linea in texto:
        re.sub(regexSignosDePuntuacion, regexReemplazo, linea)
    return texto

def crearListaDeListas(texto):
    listaDeListas = []
    for linea in texto:
        listaDePalabras = re.findall(regexPalabra, linea)
        listaDeListas.append(listaDePalabras)
    return listaDeListas

def aplanarListaDeListas(listaDeListas):
    listaAplanada = [palabra for listaDePalabras in listaDeListas for palabra in listaDePalabras]
    return listaAplanada

def contarOcurrenciaDePalabras(listaAplanada):
    contadorDePalabras = Counter(listaAplanada)
    return contadorDePalabras

def contarCantidadDePalabrasEnTotal(contadorDePalabras):
    return len(contadorDePalabras)

def obtenerLasPrimerasCincoPalabrasSegunCantidadDeOcurrencias(contadorDePalabras):
    return contadorDePalabras.most_common(LAS_PRIMERAS_CINCO)

def procesar(rutaArchivo):
    textoOriginal = abrirYLeerArchivo(rutaArchivo)
    textoEnMinusculas = solamenteMinusculas(textoOriginal)
    textoPurgado = purgadorDeSignosDePuntuacion(textoEnMinusculas)
    listaDeListas = crearListaDeListas(textoPurgado)
    listaAplanada = aplanarListaDeListas(listaDeListas)
    contadorDePalabras = contarOcurrenciaDePalabras(listaAplanada)
    mostrarResultados(contadorDePalabras)
    return contadorDePalabras #Crear nuevo archivo de texto para el siguiente punto?

def mostrarResultados(contadorDePalabras):
    print(contadorDePalabras)
    print("Cantidad de Palabras: "+str(contarCantidadDePalabrasEnTotal(contadorDePalabras)))
    print("--------------------------------------------------")
    lasCincoMasUsadas = obtenerLasPrimerasCincoPalabrasSegunCantidadDeOcurrencias(contadorDePalabras)
    print("Las cinco palabras mas usadas son: ")
    for (palabra, cantidad) in lasCincoMasUsadas:
        print(palabra)
    print("-------------------------END-------------------------")


