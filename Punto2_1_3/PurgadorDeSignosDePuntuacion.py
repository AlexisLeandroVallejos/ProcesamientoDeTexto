import re
regexSignosDePuntuacion = r'[.,;:"\\\'()\[\]{}?¿!¡—-]'
regexReemplazo = r' '

class PurgadorDeSignosDePuntuacion:
    def purgador(self, cadenaCaracteres):
        textoPurgado = re.sub(regexSignosDePuntuacion, regexReemplazo, cadenaCaracteres)
        return textoPurgado