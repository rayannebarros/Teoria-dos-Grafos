import unittest
from grafo_adj import Grafo

class TestGrafo(unittest.TestCase):

    def setUp(self):
        self.r5 = Grafo([], [])
        self.vertices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                         "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
                         "Y", "Z", "a", "b", "c", "d", "e", "f", "g"]
        self.arestas = ['A-B', 'A-C', 'A-D', 'B-E', 'B-I', 'C-G', 'D-C', 'D-H', 'E-F', 'F-B',
                        'F-J', 'G-F', 'G-J', 'G-K', 'H-G', 'H-L', 'I-M', 'J-I', 'J-N', 'K-O',
                        'L-P', 'M-Q', 'M-S', 'N-R', 'N-S', 'N-T', 'O-S', 'P-T', 'Q-U', 'R-Q',
                        'R-V', 'S-R', 'S-X', 'U-Y', 'U-Z', 'V-b', 'V-Z', 'V-W', 'W-S', 'X-c',
                        'X-d', 'Y-a', 'a-e', 'c-e', 'c-W', 'e-f', 'e-g', 'T-S']
        for i in self.vertices:
            self.r5.adiciona_vertice(i)
        for i in self.arestas:
            self.r5.adiciona_aresta(i)

    def test_dijkstra(self):
        self.assertEqual(self.r5.dijkstra(self.r5.N, self.r5.aresta_com_peso(),"G", "X", 2, ['S', 'F']),
                          "G --> F --> J --> N --> S --> X")
        self.assertEqual(self.r5.dijkstra(self.r5.N, self.r5.aresta_com_peso(),"B", "S", 1, ['I', 'E']),
                          "B --> I --> M --> S")
        self.assertEqual(self.r5.dijkstra(self.r5.N, self.r5.aresta_com_peso(),"A", "g", 3, ['L', 'S', 'U', 'a']),
                          "A --> D --> H --> L --> P --> T --> S --> X --> c --> e --> g")

        self.assertFalse(self.r5.dijkstra(self.r5.N, self.r5.aresta_com_peso(), "A", "g", 2, ['L', 'S', 'U', 'a']))
        self.assertFalse(self.r5.dijkstra(self.r5.N, self.r5.aresta_com_peso(), "A", "g", 1, ['L', 'S', 'U', 'a']))
        self.assertFalse(self.r5.dijkstra(self.r5.N, self.r5.aresta_com_peso(), "A", "g", 1, ['L', 'S', 'U', 'a']))

        self.assertEqual(self.r5.dijkstra(self.r5.N, self.r5.aresta_com_peso(), "A", "H", 3, ['D', 'G']),
                         "A --> D --> H")
        self.assertEqual(self.r5.dijkstra(self.r5.N, self.r5.aresta_com_peso(), "I", "b", 4, ['L', 'O','S','W','b']),
                         "I --> M --> S --> R --> V --> b")
