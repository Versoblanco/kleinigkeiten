import unittest
import Anagrams

class TestAnagramas(unittest.TestCase):

    def test_resultado(self):
        archivo = Anagrams.abrir_archivo('wordlist.txt')
        diccionario = Anagrams.crear_diccionario_anagramas(archivo)
        archivo.close()
        numero_conjuntos_anagramas = Anagrams.contar_conjuntos_anagramas(diccionario)
        self.assertEqual(numero_conjuntos_anagramas, 20683)

if __name__ == '__main__':
    unittest.main() 
