import unittest

from grafo_adj_nao_dir import Grafo

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        # {'a1':'J-C', 'a2':'C-E', 'a3':'C-E', 'a4':'C-P', 'a5':'C-P', 'a6':'C-M', 'a7':'C-T', 'a8':'M-T', 'a9':'T-Z'}
        self.g_p.adicionaAresta('J-C')
        self.g_p.adicionaAresta('C-E')
        self.g_p.adicionaAresta('C-E')
        self.g_p.adicionaAresta('C-P')
        self.g_p.adicionaAresta('C-P')
        self.g_p.adicionaAresta('C-M')
        self.g_p.adicionaAresta('C-T')
        self.g_p.adicionaAresta('M-T')
        self.g_p.adicionaAresta('T-Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('J-C')
        self.g_p_sem_paralelas.adicionaAresta('C-E')
        self.g_p_sem_paralelas.adicionaAresta('C-P')
        self.g_p_sem_paralelas.adicionaAresta('C-M')
        self.g_p_sem_paralelas.adicionaAresta('C-T')
        self.g_p_sem_paralelas.adicionaAresta('M-T')
        self.g_p_sem_paralelas.adicionaAresta('T-Z')

        # Grafos completos
        # self.g_c = Grafo(['J', 'C', 'E', 'P'], {'a1':'J-C', 'a3':'J-E', 'a4':'J-P', 'a6':'C-E', 'a7':'C-P', 'a8':'E-P'})
        self.g_c = Grafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('J-C')
        self.g_c.adicionaAresta('J-E')
        self.g_c.adicionaAresta('J-P')
        self.g_c.adicionaAresta('C-E')
        self.g_c.adicionaAresta('C-P')
        self.g_c.adicionaAresta('E-P')

        self.codcad = Grafo([], [])
        for i in ['1', '2', '3', '4', '5', '6']:
            self.codcad.adicionaVertice(i)
        for i in ['1-2', '1-3', '1-4', '1-6', '2-3', '2-5', '2-6', '3-4', '3-5']:
            self.codcad.adicionaAresta(i)

        self.eulergraph = Grafo([], [])
        for i in ['A', 'B', 'C', 'D', 'E', 'F']:
            self.eulergraph.adicionaVertice(i)
        for i in ['A-B', 'A-E', 'B-C', 'B-F', 'B-D', 'C-F', 'C-E', 'C-D', 'D-F', 'D-E', 'E-F']:
            self.eulergraph.adicionaAresta(i)

        # Pontes de Konigsberg
        self.konigsberg = Grafo([], [])
        for i in ['M', 'T', 'B', 'R']:
            self.konigsberg.adicionaVertice(i)
        for i in ['M-T', 'M-T', 'M-B', 'M-B', 'M-R', 'B-R', 'T-R']:
            self.konigsberg.adicionaAresta(i)

        # Grafos com caminho euleriano
        self.konigsberg_mod = Grafo([], [])
        for i in ['M', 'T', 'B', 'R']:
            self.konigsberg_mod.adicionaVertice(i)
        for i in ['M-T', 'M-T', 'M-B', 'M-B', 'M-R', 'M-R', 'B-R', 'T-R']:
            self.konigsberg_mod.adicionaAresta(i)

        self.g_c_e = Grafo([], [])
        for i in ['A', 'B', 'C']:
            self.g_c_e.adicionaVertice(i)
        for i in ['A-B', 'B-C']:
            self.g_c_e.adicionaAresta(i)

    def test_caminho_euleriano(self):
        self.assertTrue(Grafo.caminho_euleriano(self.konigsberg_mod))
        self.assertTrue(Grafo.caminho_euleriano(self.g_c_e))
        self.assertTrue(Grafo.caminho_euleriano(self.codcad))
        self.assertTrue(Grafo.caminho_euleriano(self.eulergraph))

        self.assertFalse(Grafo.caminho_euleriano(self.konigsberg))
        self.assertFalse(Grafo.caminho_euleriano(self.g_p))
        self.assertFalse(Grafo.caminho_euleriano(self.g_p_sem_paralelas))
        self.assertFalse(Grafo.caminho_euleriano(self.g_c))

    def test_procura_caminho(self):
        self.assertEquals(set(Grafo.procura_caminho_euleriano(self.g_c_e)), {'A-B', 'B-C'})
        self.assertEquals(set(Grafo.procura_caminho_euleriano(self.codcad)), {'1-2', '2-3', '3-4', '4-1', '1-3', '3-5', '5-2', '2-6', '6-1'})
        self.assertEquals(set(Grafo.procura_caminho_euleriano(self.eulergraph)), {'A-B', 'B-C', 'C-D', 'D-E', 'E-F', 'F-B', 'B-D', 'D-F', 'F-C', 'C-E', 'E-A'})
        self.assertEquals(set(Grafo.procura_caminho_euleriano(self.konigsberg_mod)), {'M-T', 'T-R', 'R-M', 'M-B', 'B-R'})

        self.assertFalse(Grafo.procura_caminho_euleriano(self.konigsberg))
        self.assertFalse(Grafo.procura_caminho_euleriano(self.g_p))
        self.assertFalse(Grafo.procura_caminho_euleriano(self.g_p_sem_paralelas))
        self.assertFalse(Grafo.procura_caminho_euleriano(self.g_c))