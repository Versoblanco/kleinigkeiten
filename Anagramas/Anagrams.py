# encoding=Utf-8
# given a file containing one word per line, print out all the combinations of words that are anagrams; each line in
# the output contains all the words from the input that are anagrams of each other.
# 1. Obtener origen palabras y crear lista ordenada.
# 2. Crear diccionario vacío
# 3. Por cada palabra de la lista: 
#   3.1 Crear anagrama ordenando sus letras en orden alfabético
#   3.2 Comprobar si el anagrama existe como clave en el diccionario. Si no existe añadir anagrama como nueva clave
#   3.3 Agregar la palabra original a la lista de valores del lema correspondiente
# 4. Presentar listas de anagramas, una por línea


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

    
def lista_palabras(archivo):
    palabras = []
    for line in archivo:
        line = line.rstrip()
        palabras.append(line)
    return palabras

def crear_diccionario(lista):
    dicc = dict()
    for i, palabra in enumerate(lista):
        anagrama = ''.join(sorted(palabra.lower()))
        if anagrama not in dicc:
            dicc[anagrama] = [palabra]
            continue
        dicc[anagrama].append(palabra)
    return dicc


def anagramas():
    #archivo = abrir_archivo(pedir_nombre_archivo())
    archivo = abrir_archivo('wordlist.txt')
    palabras = lista_palabras(archivo)
    archivo.close()
    diccionario = crear_diccionario(palabras)
    count = 0
    for lema in diccionario:
        anagramas = diccionario.get(lema)
        if len(anagramas) > 1:
            print ' - '.join(anagramas)
        count += 1
        if count > 2000000:
            exit()


if __name__ == '__main__':
    anagramas()
