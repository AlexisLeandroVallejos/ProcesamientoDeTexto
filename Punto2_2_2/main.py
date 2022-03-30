# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Punto2_2_1 import Parseador
from Punto2_2_2 import FiltroDePalabras

parser = Parseador
filter = FiltroDePalabras

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    texto = parser.obtenerTextoParseado('../king_lear.txt')
    texto = filter.filtrarTexto(texto, "../palabras_prohibidas.txt")
    parser.mostrarResultados(texto)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
