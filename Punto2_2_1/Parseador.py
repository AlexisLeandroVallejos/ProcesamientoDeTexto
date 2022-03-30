import re
from collections import Counter

LAS_PRIMERAS_CINCO = 5
regexSignosDePuntuacion = r'[.,;:"\\\'()\[\]{}?¿!¡—-]'
regexReemplazo = r' '
regexVacia = r''
regexPalabra = r'\w+'

def abrirYLeerArchivo(rutaArchivo):
    with open(rutaArchivo, 'r') as archivo:
        return archivo.read()

def solamenteMinusculas(texto):
    return texto.lower()

def purgadorDeSignosDePuntuacion(texto):
    return re.sub(regexSignosDePuntuacion, regexVacia, texto)

def contarOcurrenciaDePalabras(texto):
    return Counter(re.findall(regexPalabra, texto))

def contarCantidadDePalabrasEnTotal(contadorDePalabras: Counter):
    return sum(contadorDePalabras.values())

def obtenerLasPrimerasCincoPalabrasSegunCantidadDeOcurrencias(contadorDePalabras):
    return contadorDePalabras.most_common(LAS_PRIMERAS_CINCO)

def obtenerTextoParseado(rutaArchivo):
    texto = abrirYLeerArchivo(rutaArchivo)
    texto = solamenteMinusculas(texto)
    texto = purgadorDeSignosDePuntuacion(texto)
    return texto

def mostrarResultados(texto):
    contadorDePalabras = contarOcurrenciaDePalabras(texto)
    print(contadorDePalabras)
    print("Cantidad de Palabras: "+str(contarCantidadDePalabrasEnTotal(contadorDePalabras)))
    print("--------------------------------------------------")
    lasCincoMasUsadas = obtenerLasPrimerasCincoPalabrasSegunCantidadDeOcurrencias(contadorDePalabras)
    print("Las cinco palabras mas usadas son: ")
    for (palabra, cantidad) in lasCincoMasUsadas:
        print(palabra)
    print("-------------------------END-------------------------")
