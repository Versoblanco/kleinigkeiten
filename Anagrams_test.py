import unittest
import Anagrams

class TestAnagramas(unittest.TestCase):

    def setUp(self):
        self.anagramador = Anagrams.Anagramador()

    def test_resultado(self):
        palabras = open('wordlist.txt')
        self.assertEqual(len(self.anagramador.conjunto_anagramas(palabras)), 20683)
        palabras.close()

    def test_obtener_lista_anagramas_de_lista_palabras(self):
        palabras = ['caso', 'coche', 'saco']
        self.assertEqual([['caso', 'saco']], self.anagramador.conjunto_anagramas(palabras))

if __name__ == '__main__':
    unittest.main() 
