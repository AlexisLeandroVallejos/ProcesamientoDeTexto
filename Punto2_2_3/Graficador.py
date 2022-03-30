#!/usr/bin/python
from collections import Counter

from matplotlib import pyplot as plt


def mostrarHistograma(counter: Counter, cantidad):
    tupla = counter.most_common(cantidad)
    palabras = []
    ocurrencias = []
    for t in tupla:
        palabras.append(t[0])
        ocurrencias.append(t[1])

    xs = [i + 0.1 for i, _ in enumerate(palabras)]

    plt.bar(xs, ocurrencias)
    plt.ylabel("# Ocurrencias")
    plt.title("Palabras")

    plt.xticks([i + 0.5 for i, _ in enumerate(palabras)], palabras)
    plt.show()

def mostrarNubeDePalabras(counter: Counter, cantidad):
    tupla = counter.most_common(cantidad)
    dictionary = dict()
    for t in tupla:
        dictionary[t[0]] = t[1]
    from wordcloud import WordCloud

    wordcloud = WordCloud(background_color='white',
                          width=1500,
                          height=1000
                          ).generate_from_frequencies(dictionary)

    # use .generate(space_separated_string) - to generate cloud from text

    plt.figure(figsize=(9, 6))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
