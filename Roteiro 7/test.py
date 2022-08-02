from grafo_adj import *
from grafo_adj_nao_dir import *
import unittest


class TestGrafo(unittest.TestCase):

    def setUp(self):

        # Grafo([],[])= grafo direcionado
        # Grafo2([],[])= grafo não direcionado

        self.nao_di = Grafo2([], [])
        for i in ['A','B','C','D','E','F','G','H','I','J','K']:
            self.nao_di.adicionaVertice(i)
        for i in ['A-H','A-J','A-B','H-C','H-D','H-E','H-F','H-B','B-G','B-J','B-K','G-F','B-I','I-J','J-K','D-C','D-E']:
            self.nao_di.adicionaAresta(i)

        self.nao_di2 = Grafo2([], [])
        for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']:
            self.nao_di2.adicionaVertice(i)
        for i in ['A-B','A-J','A-H','B-C','B-D','B-E','B-F','H-B','H-G','H-J','H-K','G-F','H-I','I-J','J-K','D-C','D-E']:
            self.nao_di2.adicionaAresta(i)

        self.dire= Grafo([],[])
        for i in['A','B','C','D','E','F','G','H','I','J','K','L','M']:
            self.dire.adiciona_vertice(i)
        for i in['A-B','A-G','A-D','G-E','G-C','G-C','E-D','E-F','F-G','C-B','C-D','H-C','H-I','I-L','I-M','J-I','K-J','K-I','K-L','M-L','M-H']:
            self.dire.adiciona_aresta(i)

        self.dire2 = Grafo([], [])
        for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']:
            self.dire2.adiciona_vertice(i)
        for i in ['A-D','A-G','A-B','B-C','C-D','C-E','E-B','B-F','B-F','F-D','F-G','K-F','K-I','I-J','I-L','J-K','J-L','M-H','M-I','M-L','H-I']:
            self.dire2.adiciona_aresta(i)

    def test_busca_profundidade(self):
        self.assertEqual(self.nao_di.busca_prof_nao_dir(),
                         (['A-B', 'B-G', 'G-F', 'F-H', 'H-C', 'C-D', 'D-E', 'B-I', 'I-J', 'J-K'], ['H-A', 'H-B', 'E-H', 'D-H', 'J-A', 'J-B', 'K-B']))
        self.assertEqual(self.nao_di2.busca_prof_nao_dir(),
                         (['A-B', 'B-C', 'C-D', 'D-E', 'B-F', 'F-G', 'G-H', 'H-I', 'I-J', 'J-K'], ['D-B', 'E-B', 'H-A', 'H-B', 'J-A', 'J-H', 'K-H']))
        self.assertEqual(self.dire.busca_profundidade_dir(),
                         (['A-B', 'A-D', 'A-G', 'G-C', 'G-E', 'E-F', 'H-I', 'I-L', 'I-M'], ['G-C', 'F-G', 'M-H'], ['C-B', 'C-D', 'E-D', 'H-C', 'M-L', 'J-I', 'K-I', 'K-J', 'K-L']))
        self.assertEqual(self.dire2.busca_profundidade_dir(),
                         (['A-B', 'B-C', 'C-D', 'C-E', 'B-F', 'F-G', 'H-I', 'I-J', 'J-K', 'J-L'], ['E-B', 'B-F', 'A-D', 'A-G', 'K-I', 'I-L'], ['F-D', 'K-F', 'M-H', 'M-I', 'M-L']))
