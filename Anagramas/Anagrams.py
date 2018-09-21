# given a file containing one word per line, print out all the combinations of words that are anagrams; each line in
# the output contains all the words from the input that are anagrams of each other.
# Paso 1: Definir lista de palabras (pte. extraer desde archivo)
# Paso 2: Ordenar letras de cada palabra en orden alfabetico en lista nueva
# Paso 3: Indexar palabras iguales
# Paso 4: Extraer palabras indexadas
# Paso 5 Repetir pasos 3-4 hasta vaciar lista
# Paso 6: Presentar lista de anagramas


def lista_palabras():
    palabras = ["roma",  "mora", "ramo", "concha", "perro", "mira", "amor", "rima"]
    return palabras


def lista_abc(palabras):
    abc = map(sorted, palabras)
    return map(''.join, abc)


def indexar(abc):
    ind = []
    for i in range(len(abc)):
        if abc[i] == abc[0]:
            ind.append(i)
        else:
            continue
    return ind


def extraer(palabras, abc, ind):
    extracto = []
    for i, posicion in enumerate(ind):
        posicion = posicion - i
        extracto.append(palabras.pop(posicion))
        del abc[posicion]
    return extracto


def anagramas():
    palabras = lista_palabras()
    abc = lista_abc(palabras)
    while len(palabras) > 0:
        ind = indexar(abc)
        print extraer(palabras, abc, ind)

if __name__ == '__main__':
    anagramas()
