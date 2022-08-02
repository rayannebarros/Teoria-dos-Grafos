import unittest
from grafo_adj import *

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = Grafo([], [])
        for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
            self.g_p.adiciona_vertice(i)
        for i in ['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
            self.g_p.adiciona_aresta(i)

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = Grafo([], [])
        for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
            self.g_p_sem_paralelas.adiciona_vertice(i)
        for i in ['J-C', 'C-E', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
            self.g_p_sem_paralelas.adiciona_aresta(i)

        # Grafos completos
        self.g_c = Grafo([], [])
        for i in ['J', 'C', 'E', 'P']:
            self.g_c.adiciona_vertice(i)
        for i in ['J-C', 'J-E', 'J-P', 'C-J', 'C-E', 'C-P', 'E-J', 'E-C', 'E-P', 'P-J', 'P-C', 'P-E']:
            self.g_c.adiciona_aresta(i)


        self.g_c3 = Grafo([], [])
        self.g_c3.adiciona_vertice('J')

        # Grafos com laco
        self.g_l1 = Grafo([], [])
        for i in ['A', 'B', 'C', 'D']:
            self.g_l1.adiciona_vertice(i)
        for i in ['A-A', 'B-A', 'A-A']:
            self.g_l1.adiciona_aresta(i)

        self.g_l2 = Grafo([], [])
        for i in ['A', 'B', 'C', 'D']:
            self.g_l2.adiciona_vertice(i)
        for i in ['A-B', 'B-B', 'B-A']:
            self.g_l2.adiciona_aresta(i)

        self.g_l3 = Grafo([], [])
        for i in ['A', 'B', 'C', 'D']:
            self.g_l3.adiciona_vertice(i)
        for i in ['C-A', 'C-C', 'D-D']:
            self.g_l3.adiciona_aresta(i)

        self.g_l4 = Grafo([], [])
        self.g_l4.adiciona_vertice('D')
        self.g_l4.adiciona_aresta('D-D')

        self.g_l5 = Grafo([], [])
        for i in ['C', 'D']:
            self.g_l5.adiciona_vertice(i)
        for i in ['D-C', 'C-C']:
            self.g_l5.adiciona_aresta(i)

        self.henrique = Grafo([], [])
        for i in ['A', 'B', 'C', 'D']:
            self.henrique.adiciona_vertice(i)
        for i in ['A-B', 'B-D', 'D-C', 'C-B', 'C-D']:
            self.henrique.adiciona_aresta(i)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(set(Grafo.vertices_nao_adjacentes(self.g_p)), set(['J-J', 'J-E', 'J-P', 'J-M', 'J-T', 'J-Z',
                                                                      'C-J', 'C-C', 'C-Z',
                                                                      'E-J', 'E-C', 'E-E', 'E-P', 'E-M', 'E-T', 'E-Z',
                                                                      'P-J', 'P-C', 'P-E', 'P-P', 'P-M', 'P-T', 'P-Z',
                                                                      'M-J', 'M-C', 'M-E', 'M-P', 'M-M', 'M-Z',
                                                                      'T-J', 'T-C', 'T-E', 'T-P','T-M', 'T-T',
                                                                      'Z-J', 'Z-C', 'Z-E', 'Z-P', 'Z-M', 'Z-T', 'Z-Z']))

        self.assertEqual(Grafo.vertices_nao_adjacentes(self.g_c), ['J-J', 'C-C', 'E-E', 'P-P'])

        self.assertEqual(Grafo.vertices_nao_adjacentes(self.g_c3), ['J-J'])

    def test_ha_laco(self):
        self.assertFalse(Grafo.ha_laco(self.g_p))
        self.assertFalse(Grafo.ha_laco(self.g_p_sem_paralelas))
        self.assertTrue(Grafo.ha_laco(self.g_l1))
        self.assertTrue(Grafo.ha_laco(self.g_l2))
        self.assertTrue(Grafo.ha_laco(self.g_l3))
        self.assertTrue(Grafo.ha_laco(self.g_l4))
        self.assertTrue(Grafo.ha_laco(self.g_l5))

    def test_grau(self):
        # Paraíba
        self.assertEqual(Grafo.grau(self.g_p, 'J'), 1)
        self.assertEqual(Grafo.grau(self.g_p, 'C'), 7)
        self.assertEqual(Grafo.grau(self.g_p, 'E'), 2)
        self.assertEqual(Grafo.grau(self.g_p, 'P'), 2)
        self.assertEqual(Grafo.grau(self.g_p, 'M'), 2)
        self.assertEqual(Grafo.grau(self.g_p, 'T'), 3)
        self.assertEqual(Grafo.grau(self.g_p, 'Z'), 1)

        # Completos
        self.assertEqual(Grafo.grau(self.g_c, 'J'), 6)
        self.assertEqual(Grafo.grau(self.g_c, 'C'), 6)
        self.assertEqual(Grafo.grau(self.g_c, 'E'), 6)
        self.assertEqual(Grafo.grau(self.g_c, 'P'), 6)

        # Com laço. Lembrando que cada laço conta uma única vez por vértice para cálculo do grau
        self.assertEqual(Grafo.grau(self.g_l1, 'A'), 3)
        self.assertEqual(Grafo.grau(self.g_l2, 'B'), 3)
        self.assertEqual(Grafo.grau(self.g_l4, 'D'), 1)

    def test_arestas_ha_paralelas(self):
        self.assertTrue(Grafo.ha_paralelas(self.g_p))
        self.assertFalse(Grafo.ha_paralelas(self.g_p_sem_paralelas))
        self.assertFalse(Grafo.ha_paralelas(self.g_c))
        self.assertFalse(Grafo.ha_paralelas(self.g_c3))
        self.assertTrue(Grafo.ha_paralelas(self.g_l1))

    def test_arestas_sobre_vertice(self):
        self.assertEqual(set(Grafo.arestas_sobre_vertice(self.g_p, 'J')), {'J-C'})
        self.assertEqual(set(Grafo.arestas_sobre_vertice(self.g_p, 'C')), {'J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T'})
        self.assertEqual(set(Grafo.arestas_sobre_vertice(self.g_p, 'M')), {'C-M', 'M-T'})

    def test_eh_completo(self):
        self.assertFalse(Grafo.eh_completo(self.g_p))
        self.assertFalse(Grafo.eh_completo(self.g_p_sem_paralelas))
        self.assertTrue(Grafo.eh_completo(self.g_c))
        self.assertTrue(Grafo.eh_completo(self.g_c3))
        self.assertFalse(Grafo.eh_completo(self.g_l1))
        self.assertFalse(Grafo.eh_completo(self.g_l2))
        self.assertFalse(Grafo.eh_completo(self.g_l3))
        self.assertTrue(Grafo.eh_completo(self.g_l4))
        self.assertFalse(Grafo.eh_completo(self.g_l5))

    def test_warshall(self):
        self.assertEquals(Grafo.warshall(self.g_p), [[0, 1, 1, 1, 1, 1, 1],
                                                     [0, 0, 1, 1, 1, 1, 1],
                                                     [0, 0, 0, 0, 0, 0, 0],
                                                     [0, 0, 0, 0, 0, 0, 0],
                                                     [0, 0, 0, 0, 0, 1, 1],
                                                     [0, 0, 0, 0, 0, 0, 1],
                                                     [0, 0, 0, 0, 0, 0, 0]])

        self.assertEquals(Grafo.warshall(self.g_p_sem_paralelas), [[0, 1, 1, 1, 1, 1, 1],
                                                                   [0, 0, 1, 1, 1, 1, 1],
                                                                   [0, 0, 0, 0, 0, 0, 0],
                                                                   [0, 0, 0, 0, 0, 0, 0],
                                                                   [0, 0, 0, 0, 0, 1, 1],
                                                                   [0, 0, 0, 0, 0, 0, 1],
                                                                   [0, 0, 0, 0, 0, 0, 0]])

        self.assertEquals(Grafo.warshall(self.henrique), [[0, 1, 1, 1],
                                                          [0, 1, 1, 1],
                                                          [0, 1, 1, 1],
                                                          [0, 1, 1, 1]])

        self.assertEquals(Grafo.warshall(self.g_c), [[1, 1, 1, 1],
                                                     [1, 1, 1, 1],
                                                     [1, 1, 1, 1],
                                                     [1, 1, 1, 1]])

        self.assertEquals(Grafo.warshall(self.g_l1), [[1, 0, 0, 0],
                                                      [1, 0, 0, 0],
                                                      [0, 0, 0, 0],
                                                      [0, 0, 0, 0]])