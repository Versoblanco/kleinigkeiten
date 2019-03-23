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


def anagramas():
    #archivo = abrir_archivo(pedir_nombre_archivo())
    archivo = abrir_archivo('wordlist.txt')
    diccionario = crear_diccionario_anagramas(archivo)
    archivo.close()
    for clave in diccionario:
        anagramas = diccionario.get(clave)
        if len(anagramas) > 1:
            print ' - '.join(anagramas)
    print len(diccionario)


if __name__ == '__main__':
    anagramas()
