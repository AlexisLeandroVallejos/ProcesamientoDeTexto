import re
regexNumerosRomanosValidos = '[IVXLCDM\s*]'

class AnalizadorNumerosRomanos:
    def sonTodosSimbolosDeNumerosRomanos(self, cadenaCaracteres):
        listaDeVerdad = []
        for caracter in cadenaCaracteres:
            numeroRomanoValido = re.search(regexNumerosRomanosValidos, caracter)
            if numeroRomanoValido: #Es un tipo Match si matchea, no es exactamente Bool
                listaDeVerdad.append(True)
            else:
                listaDeVerdad.append(False)
        return all(listaDeVerdad)