#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
from grafo_adj import *


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = Grafo([], [])
        for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
            self.g_p.adiciona_vertice(i)
        for i in [['J-C', 3], ['C-E', 7], ['C-E', 2], ['C-P', 6], ['C-P', 2], ['C-M', 5], ['C-T', 9], ['M-T', 7], ['T-Z', 4]]:
            self.g_p.adiciona_aresta(i)

        # Grafos completos
        self.g_c = Grafo([], [])
        for i in ['J', 'C', 'E', 'P']:
            self.g_c.adiciona_vertice(i)
        for i in [['J-C', 5], ['J-E', 10], ['J-P', 8], ['C-J', 9], ['C-E', 7], ['C-P', 1], ['E-J', 7], ['E-C', 4],
                  ['E-P', 6], ['P-J', 3], ['P-C', 9], ['P-E', 2]]:
            self.g_c.adiciona_aresta(i)

        self.g_c3 = Grafo([], [])
        self.g_c3.adiciona_vertice('J')

        # Grafos com laco
        self.g_l1 = Grafo([], [])
        for i in ['A', 'B', 'C', 'D']:
            self.g_l1.adiciona_vertice(i)
        for i in [['A-A', 7], ['B-A', 8], ['A-A', 10]]:
            self.g_l1.adiciona_aresta(i)

        self.g_l4 = Grafo([], [])
        self.g_l4.adiciona_vertice('D')
        self.g_l4.adiciona_aresta(['D-D', 1])

        self.g_l5 = Grafo([], [])
        for i in ['C', 'D']:
            self.g_l5.adiciona_vertice(i)
        for i in [['D-C', 5], ['C-C', 1]]:
            self.g_l5.adiciona_aresta(i)

        self.g_challenger = Grafo([], [])
        for i in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "X", "Y", "W", "Z", "1", "2", "3", "4", "5", "6", "7"]:
            self.g_challenger.adiciona_vertice(i)
        for i in [['A-B', 5], ['A-C', 3], ['A-D', 10], ['B-H', 2], ['B-I', 8], ['C-F', 9], ['D-C', 3], ['D-E', 7],
                  ['E-F', 1], ['E-L', 3], ['F-G', 3], ['F-J', 4], ['F-K', 5], ['G-B', 3], ['G-J', 6], ['H-G', 4],
                  ['I-P', 8], ['J-I', 5], ['J-O', 6], ['K-N', 9], ['L-M', 4], ['M-Q', 8], ['N-R', 7], ['O-5', 7], ['O-R', 6],
                  ['O-Q', 9], ['P-R', 10], ['P-T', 2], ['Q-R', 9], ['R-5', 6],['R-Y', 10],['T-U', 6], ['U-7', 8], ['U-W', 10],
                  ['V-2', 5], ['V-W', 8], ['V-X', 1], ['X-R', 6], ['Y-Z', 1], ['Y-1', 2], ['1-3', 1], ['1-X', 9], ['3-4', 3],
                  ['3-S', 4], ['5-T', 3], ['5-V', 6], ['6-3', 8], ['7-6', 9]]:
            self.g_challenger.adiciona_aresta(i)


    def test_Prim(self):
        self.assertEqual(self.g_p.Prim(), {'a1': ['J-C', 3],'a3': ['C-E', 2], 'a5': ['C-P', 2],'a6': ['C-M', 5],
                                           'a8': ['M-T', 7],'a9': ['T-Z', 4]})
        self.assertEqual(self.g_c.Prim(), {'a10': ['P-J', 3], 'a12': ['P-E', 2], 'a6': ['C-P', 1]})
        self.assertEqual(self.g_c3.Prim(), {})
        self.assertFalse(self.g_l1.Prim())
        self.assertEqual(self.g_l4.Prim(), {})
        self.assertEqual(self.g_l5.Prim(), {"a1": ['D-C', 5]})
        self.assertEqual(self.g_challenger.Prim(), {'a1': ['A-B', 5],'a10': ['E-L', 3],'a11': ['F-G', 3],
                                                    'a12': ['F-J', 4],'a13': ['F-K', 5],'a14': ['G-B', 3],
                                                    'a18': ['J-I', 5],'a19': ['J-O', 6],'a2': ['A-C', 3],
                                                    'a21': ['L-M', 4],'a22': ['M-Q', 8],'a23': ['N-R', 7],
                                                    'a25': ['O-R', 6],'a28': ['P-T', 2],'a30': ['R-5', 6],
                                                    'a32': ['T-U', 6],'a33': ['U-7', 8],'a35': ['V-2', 5],
                                                    'a36': ['V-W', 8],'a37': ['V-X', 1],'a38': ['X-R', 6],
                                                    'a39': ['Y-Z', 1],'a4': ['B-H', 2],'a40': ['Y-1', 2],
                                                    'a41': ['1-3', 1],'a42': ['1-X', 9],'a43': ['3-4', 3],
                                                    'a44': ['3-S', 4],'a45': ['5-T', 3],'a47': ['6-3', 8],
                                                    'a7': ['D-C', 3],'a9': ['E-F', 1]})

    def test_opPrim(self):
        self.assertEqual(self.g_p.opPrim(),  {'a1': ['J-C', 3], 'a3': ['C-E', 2], 'a5': ['C-P', 2], 'a6': ['C-M', 5],
                                            'a8': ['M-T', 7], 'a9': ['T-Z', 4]})
        self.assertEqual(self.g_c.opPrim(), {'a10': ['P-J', 3], 'a12': ['P-E', 2], 'a6': ['C-P', 1]})
        self.assertEqual(self.g_c3.opPrim(), {})
        self.assertFalse(self.g_l1.opPrim())
        self.assertEqual(self.g_l4.opPrim(), {})
        self.assertEqual(self.g_l5.opPrim(), {"a1": ['D-C', 5]})
        self.assertEqual(self.g_challenger.opPrim(), {'a1': ['A-B', 5], 'a2': ['A-C', 3], 'a7': ['D-C', 3],
                                                    'a11': ['F-G', 3], 'a9': ['E-F', 1], 'a4': ['B-H', 2],
                                                    'a18': ['J-I', 5], 'a14': ['G-B', 3], 'a12': ['F-J', 4],
                                                    'a13': ['F-K', 5], 'a10': ['E-L', 3], 'a21': ['L-M', 4],
                                                    'a22': ['M-Q', 8], 'a19': ['J-O', 6], 'a23': ['N-R', 7],
                                                    'a28': ['P-T', 2], 'a30': ['R-5', 6], 'a25': ['O-R', 6],
                                                    'a40': ['Y-1', 2], 'a38': ['X-R', 6], 'a45': ['5-T', 3],
                                                    'a37': ['V-X', 1], 'a32': ['T-U', 6], 'a41': ['1-3', 1],
                                                    'a35': ['V-2', 5], 'a36': ['V-W', 8], 'a33': ['U-7', 8],
                                                    'a48': ['7-6', 9], 'a47': ['6-3', 8], 'a43': ['3-4', 3],
                                                    'a44': ['3-S', 4], 'a39': ['Y-Z', 1]})

    def test_Kruskall(self):
        self.assertEqual(self.g_p.Kruskall(), {'a1': ['J-C', 3], 'a3': ['C-E', 2], 'a5': ['C-P', 2], 'a6': ['C-M', 5],
                                               'a8': ['M-T', 7], 'a9': ['T-Z', 4]})
        self.assertEqual(self.g_c3.Kruskall(), {})
        self.assertFalse(self.g_l1.Kruskall())
        self.assertFalse(self.g_l4.Kruskall())
        self.assertEqual(self.g_l5.Kruskall(), {"a1": ['D-C', 5]})
        self.assertEqual(self.g_challenger.Kruskall(), {'a1': ['A-B', 5], 'a10': ['E-L', 3], 'a11': ['F-G', 3],
                                                        'a12': ['F-J', 4], 'a13': ['F-K', 5], 'a14': ['G-B', 3],
                                                        'a18': ['J-I', 5], 'a19': ['J-O', 6], 'a2': ['A-C', 3],
                                                        'a21': ['L-M', 4], 'a22': ['M-Q', 8], 'a23': ['N-R', 7],
                                                        'a25': ['O-R', 6], 'a28': ['P-T', 2], 'a30': ['R-5', 6],
                                                        'a32': ['T-U', 6], 'a33': ['U-7', 8], 'a35': ['V-2', 5],
                                                        'a36': ['V-W', 8], 'a37': ['V-X', 1], 'a38': ['X-R', 6],
                                                        'a39': ['Y-Z', 1], 'a4': ['B-H', 2], 'a40': ['Y-1', 2],
                                                        'a41': ['1-3', 1], 'a42': ['1-X', 9], 'a43': ['3-4', 3],
                                                        'a44': ['3-S', 4], 'a45': ['5-T', 3], 'a47': ['6-3', 8],
                                                        'a7': ['D-C', 3], 'a9': ['E-F', 1]})

    def test_opKruskall(self):
        self.assertEqual(self.g_p.opKruskall(), {'a1': ['J-C', 3], 'a3': ['C-E', 2], 'a5': ['C-P', 2], 'a6': ['C-M', 5],
                                                 'a8': ['M-T', 7], 'a9': ['T-Z', 4]})
        self.assertEqual(self.g_c3.opKruskall(), {})
        self.assertFalse(self.g_l1.opKruskall())
        self.assertFalse(self.g_l4.opKruskall())
        self.assertEqual(self.g_l5.opKruskall(), {"a1": ['D-C', 5]})
        self.assertEqual(self.g_challenger.opKruskall(), {'a1': ['A-B', 5], 'a10': ['E-L', 3], 'a11': ['F-G', 3],
                                                          'a12': ['F-J', 4], 'a13': ['F-K', 5], 'a14': ['G-B', 3],
                                                          'a18': ['J-I', 5], 'a19': ['J-O', 6], 'a2': ['A-C', 3],
                                                          'a21': ['L-M', 4], 'a22': ['M-Q', 8], 'a23': ['N-R', 7],
                                                          'a25': ['O-R', 6], 'a28': ['P-T', 2], 'a30': ['R-5', 6],
                                                          'a32': ['T-U', 6], 'a33': ['U-7', 8], 'a35': ['V-2', 5],
                                                          'a36': ['V-W', 8], 'a37': ['V-X', 1], 'a38': ['X-R', 6],
                                                          'a39': ['Y-Z', 1], 'a4': ['B-H', 2], 'a40': ['Y-1', 2],
                                                          'a41': ['1-3', 1], 'a42': ['1-X', 9], 'a43': ['3-4', 3],
                                                          'a44': ['3-S', 4], 'a45': ['5-T', 3], 'a47': ['6-3', 8],
                                                          'a7': ['D-C', 3], 'a9': ['E-F', 1]})
