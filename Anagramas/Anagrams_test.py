import unittest
import Anagrams

class TestAnagramas(unittest.TestCase):

    def test_resultado(self):
        palabras = open('wordlist.txt')
        numero_conjuntos_anagramas = Anagrams.Anagramador().contar_conjuntos_anagramas(palabras)
        palabras.close()
        
        self.assertEqual(numero_conjuntos_anagramas, 20683)

    def test_obtener_lista_anagramas_de_lista_palabras(self):
        palabras = ['caso', 'coche', 'saco']
        self.assertEqual([['caso', 'saco']], Anagrams.Anagramador().conjunto_anagramas(palabras))

if __name__ == '__main__':
    unittest.main() 
