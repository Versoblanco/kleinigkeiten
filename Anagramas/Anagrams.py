# encoding=Utf-8
# http://codekata.com/kata/kata06-anagrams/
# Given a file containing one word per line, print out all the combinations of words that are anagrams; each line in the output contains all the words from the input that are anagrams of each other.
# For added programming pleasure, find the longest words that are anagrams, and find the set of anagrams containing the most words (so “parsley players replays sparely” would not win, having only four words in the set)
# 1. Obtener palabras de archivo de origen
# 2. Crear diccionario vacío
# 3. Por cada palabra del archivo (1 palabra x línea): 
#   3.1 Crear anagrama ordenando sus letras en orden alfabético
#   3.2 Comprobar si el anagrama ya está en el diccionario, si no existe añadirlo como lema.
#   3.3 Agregar la palabra a la lista de valores de su lema.
# 4. Presentar anagramas, una lista por línea, excluyendo las palabras que sólo aparecen una vez.

# PROBLEMAS: Los anagramas se clasifican en minúsculas, pero la lista respeta la ortografía original, duplicación de homógrafos con distinta capitalización.


def pedir_nombre_archivo():
    nombre = raw_input('Enter a file name: ')
    return nombre


def abrir_archivo(nombre):
    try:
        archivo = open(nombre)
        return archivo
    except:
        print 'File cannot be open'
        exit()


def crear_diccionario_anagramas(palabras):
    dicc = {}
    for palabra in palabras:
        palabra = palabra.rstrip()
        anagrama = ''.join(sorted(palabra))
        if anagrama not in dicc:
            dicc[anagrama] = [palabra]
            continue
        dicc[anagrama].append(palabra)
    return dicc

def contar_conjuntos_anagramas(diccionario):
    numero_conjuntos_anagramas = 0
    for clave in diccionario:
        palabras = diccionario.get(clave)
        if es_conjunto_anagramas(palabras):
            numero_conjuntos_anagramas = numero_conjuntos_anagramas + 1
    return numero_conjuntos_anagramas

def es_conjunto_anagramas(palabras):
    return len(palabras) > 1

def anagramas():
    archivo = abrir_archivo('wordlist.txt')
    diccionario = crear_diccionario_anagramas(archivo)
    archivo.close()
    numero_conjuntos_anagramas = contar_conjuntos_anagramas(diccionario)
    if numero_conjuntos_anagramas == 20683:
        print "ok"
    else:
        print "error you got {} instead of 20683".format(numero_conjuntos_anagramas)

if __name__ == '__main__':
    anagramas()
