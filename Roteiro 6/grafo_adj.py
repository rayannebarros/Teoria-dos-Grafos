#!/usr/bin/python3

'''
Micael Marques Rodrigues Silva
Rayanne Kelly Marcelino Barros Elias
'''

from copy import copy, deepcopy
from math import inf

class VerticeInvalidoException(Exception):
    pass

class ArestaInvalidaException(Exception):
    pass

class MatrizInvalidaException(Exception):
    pass

class Grafo:

    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'
    __maior_vertice = 0

    def __init__(self, N=[], M=[]):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param N: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma matriz de adjacência que guarda as arestas do grafo. Cada entrada da matriz tem um inteiro que indica a quantidade de arestas que ligam aqueles vértices
        '''
        self.vertices_byRecursion = []
        self.verify = True
        for v in N:
            if not(Grafo.vertice_valido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

        self.N = N

        """
        g
          C D
        C 1 0 
        D 1 0 
        """
        self.minE = None
        self.maxE = None
        self.MD = {}  # g.MD = {'a0': ['D-C', 1], 'a1': ['C-C', 1]}
        self.VA = {}  # {'D': ['a1'], 'C': ['a1', 'a2']}g
        self.counter = 1  # contador para a gravação das chaves (arestas) do self.MD { "a{}".format(selfcounter) }

        if len(M) != len(N):
            raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for c in M:
            if len(c) != len(N):
                raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for i in range(len(N)):
            for j in range(len(N)):
                aresta = N[i] + Grafo.SEPARADOR_ARESTA + N[j]
                if not(self.aresta_valida(aresta)):
                    raise ArestaInvalidaException('A aresta ' + aresta + ' é inválida')

        self.M = M

    def aresta_valida(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta é representada por um string com o formato a-b, onde:
        a é um substring de aresta que é o nome de um vértice adjacente à aresta.
        - é um caractere separador. Uma aresta só pode ter um único caractere como esse.
        b é um substring de aresta que é o nome do outro vértice adjacente à aresta.
        Além disso, uma aresta só é válida se conectar dois vértices existentes no grafo.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        '''

        # Não pode haver mais de um caractere separador
        if aresta.count(Grafo.SEPARADOR_ARESTA) != Grafo.QTDE_MAX_SEPARADOR:
            return False

        # Índice do elemento separador
        i_traco = aresta.index(Grafo.SEPARADOR_ARESTA)

        # O caractere separador não pode ser o primeiro ou o último caractere da aresta
        if i_traco == 0 or aresta[-1] == Grafo.SEPARADOR_ARESTA:
            return False

        if not(self.existe_vertice(aresta[:i_traco])) or not(self.existe_vertice(aresta[i_traco + 1:])):
            return False

        return True

    @classmethod
    def vertice_valido(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existe_vertice(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.vertice_valido(vertice) and self.N.count(vertice) > 0

    def primeiro_vertice_aresta(self, a: str):
        return a[0:a.index(Grafo.SEPARADOR_ARESTA)]

    def segundo_vertice_aresta(self, a: str):
        return a[a.index(Grafo.SEPARADOR_ARESTA)+1:]

    def indice_primeiro_vertice_aresta(self, a: str):
        return self.N.index(self.primeiro_vertice_aresta(a))

    def indice_segundo_vertice_aresta(self, a: str):
        return self.N.index(self.segundo_vertice_aresta(a))

    def existe_aresta(self, a: str):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.aresta_valida(self, a):
            for i in range(len(self.M)):
                for j in range(len(self.M)):
                    if self.M[self.indice_primeiro_vertice_aresta(a)][self.indice_segundo_vertice_aresta(a)]:
                        existe = True

        return existe

    def adiciona_vertice(self, v):
        if self.vertice_valido(v):
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

            self.N.append(v)
            self.M.append([])
            for k in range(len(self.N)):
                if k != len(self.N) -1:
                    self.M[k].append(0)
                self.M[self.N.index(v)].append(0)
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adiciona_aresta(self, a):
        peso = a[-1]
        if self.aresta_valida(a[0]) and self.peso_valido(peso):
            self.M[self.indice_primeiro_vertice_aresta(a[0])][self.indice_segundo_vertice_aresta(a[0])] += 1
            aresta = "a{}".format(self.counter)
            self.counter += 1
            self.MD[aresta] = [a[0], peso]
            if self.minE is None:
                self.minE = aresta
            elif peso < self.MD[self.minE][-1]:
                self.minE = aresta
            if self.maxE is None:
                self.maxE = aresta
            elif peso > self.MD[self.maxE][-1]:
                self.maxE = aresta
            if a[0][0] in self.VA.keys():
                if aresta not in self.VA[a[0][0]]:
                    self.VA[a[0][0]].append(aresta)
            else:
                self.VA[a[0][0]] = [aresta]
            if a[0][-1] in self.VA.keys():
                if aresta not in self.VA[a[0][-1]]:
                    self.VA[a[0][-1]].append(aresta)
            else:
                self.VA[a[0][-1]] = [aresta]
        else:
            ArestaInvalidaException('A aresta ' + self.A[a[0]] + ' é inválida')

    def peso_valido(self, p):
        if 0 < p < inf:
            return True
        return False

    def heap(self, dit):
        lis = list(dit.values())
        lis.sort(key=lambda a: a[-1])
        di = {}
        for a in lis:
            di[self.ares(a)] = a
        return di

    def conf(self):
        sonf = {}
        for v in self.N:
            sonf[v] = 0
        return sonf

    def ares(self, valor):
        for k in self.MD.keys():
            if self.MD[k] == valor:
                return k

    def flo(self):
        dit = {}
        for v in self.N:
            dit[v] = []
        return dit

    def mesma_arv_fixed(self, floresta, aa, ab):
        self.verify = False
        self.mesma_arvore_r_fixed(floresta, aa, ab)
        return self.verify

    def mesma_arvore_r_fixed(self, floresta, aa, ab):
        if aa == ab:
            pass
        self.vertices_byRecursion.append(aa)
        for v in floresta[aa]:
            if v not in self.vertices_byRecursion:
                self.mesma_arvore_r_fixed(floresta, v, ab)

    def opHeap(self, dit):
        if None in [self.minE, self.maxE]:
            return {}
        lis = list(dit.values())
        buckets = {}
        ma = self.MD[self.maxE][-1]
        me = self.MD[self.minE][-1]
        b = (ma - me + 1) * 0.3
        for ed in lis:
            w = ed[-1]
            if ma == me:
                ma += 1
            bucket_number = int(((w - me)/(ma - me))*(b - 1)) + 1
            if "bucket{}".format(bucket_number) not in buckets.keys():
                buckets["bucket{}".format(bucket_number)] = [ed]
            else:
                buckets["bucket{}".format(bucket_number)].append(ed)
        ret = {}
        for b in sorted(buckets.keys()):
            buckets[b].sort(key=lambda a: a[-1])
            for ed in buckets[b]:
                ret[self.ares(ed)] = ed
        return ret

    def opKruskall(self):
        heap = self.opHeap(self.MD)
        floresta = self.flo()
        vertices = []
        arestas = {}
        if len(heap) > 0:
            for a in heap:
                aa = heap[a][0][0]
                ab = heap[a][0][-1]
                if not self.mesma_arv_fixed(floresta, aa, ab):
                    floresta[aa].append(ab)
                    floresta[ab].append(aa)
                    arestas[a] = self.MD[a]
                    if aa not in vertices:
                        vertices.append(aa)
                    if ab not in vertices:
                        vertices.append(ab)
        else:
            return heap
        if len(vertices) != len(self.N):
            return "não é conexo"
        return arestas

    def vSet(self):
        return deepcopy(self.VA)

    def aSet(self):
        return deepcopy(self.MD)

    def jet_parentSet(self):
        jet = {}
        parent = {}
        for v in self.N:
            jet[v] = inf
            parent[v] = None
        return (jet, parent)

    def minEdge(self, E):
        Min = {}
        for k in E.keys():
            if Min != {} and E[k][-1] < Min[list(Min.keys())[0]][-1]:
                Min.clear()
                Min[k] = E[k]
            else:
                Min = E[k]
        return Min

    def minQueue(self, V):
        lis = list(V.items())
        lis.sort(key=lambda a: a[-1])
        return lis

    def extract(self, R, M):
        for t in M:
            if t[0] == R:
                M.remove(t)

    def adj(self, R):
        ver = {}
        for k in self.VA[R]:
            if self.MD[k][0][0] != R:
                if self.MD[k][0][0] not in ver.keys():
                    ver[self.MD[k][0][0]] = self.MD[k][-1]
                else:
                    if self.MD[k][-1] < ver[self.MD[k][0][0]]:
                        ver[self.MD[k][0][0]] = self.MD[k][-1]
            elif self.MD[k][0][-1] != R:
                if self.MD[k][0][-1] not in ver.keys():
                    ver[self.MD[k][0][-1]] = self.MD[k][-1]
                else:
                    if self.MD[k][-1] < ver[self.MD[k][0][-1]]:
                        ver[self.MD[k][0][-1]] = self.MD[k][-1]
        return ver

    def heap_map(self):
        map = {}
        for v in self.N:
            map[v] = inf
        return map

    def Min(self, heap_map):
        try:
            m = min(heap_map.values())
        except:
            return "heap_vazio"
        k = None
        if m != inf:
            for v in heap_map.keys():
                if heap_map[v] == m:
                    k = v
        if k is None:
            return 'não é conexo'
        return k

    def adjt(self, v, heap_map):
        lis = []
        for a in self.VA[v]:
            for c in self.MD[a][0]:
                if c != "-":
                    if c != v and c not in lis and c in heap_map.keys():
                        lis.append(c)
                        break
        return lis

    def menor_aresta(self, v, m, ev):
        mm = None
        arestas = []
        for a in self.VA[v]:
            if self.MD[a][0] != self.MD[a][-1]:
                if self.MD[a][0] not in ev.keys() or self.MD[a][-1] not in ev.keys():
                    arestas.append(a)
        for a in arestas:
            if v in self.MD[a][0] and m in self.MD[a][0]:
                if mm is None:
                    mm = a
                elif self.MD[a][-1] < self.MD[mm][-1]:
                    mm = a
        return mm

    def Prim_indian(self):
        heap_map = self.heap_map()
        EV_map = {}
        heap_map[self.N[0]] = 0
        while True:
            m = self.Min(heap_map)
            if m == "não é conexo":
                return "não é conexo"
            elif m == "heap_vazio":
                break
            else:
                heap_map.pop(m)
                vertices_adj = self.adjt(m, heap_map)
                for v in vertices_adj:
                    menor_aresta = self.menor_aresta(v, m, EV_map)
                    heap_map[v] = self.MD[menor_aresta][-1]
                    if v not in EV_map.keys():
                        EV_map[v] = menor_aresta
                    else:
                        if self.MD[menor_aresta][-1] < self.MD[EV_map[v]][-1]:
                            EV_map[v] = menor_aresta
        dit = {}
        for a in EV_map.values():
            dit[a] = self.MD[a]
        return dit

    def verticeOp(self):
        minorEdge = None
        for a in self.MD.keys():
            if minorEdge is None:
                minorEdge = a
            elif self.MD[a][-1] < self.MD[minorEdge][-1]:
                minorEdge = a
        if minorEdge is not None:
            return self.MD[minorEdge][0][0]
        return "heap_vazio"

    def opPrim(self):
        heap_map = self.heap_map()
        EV_map = {}
        vertice_inicial = self.verticeOp()
        heap_map[vertice_inicial] = 0
        firstCall = True
        while True:
            if firstCall:
                m = vertice_inicial
                firstCall = False
            else:
                m = self.Min(heap_map)
            if m == "não é conexo":
                return "não é conexo"
            elif m == "heap_vazio":
                break
            else:
                heap_map.pop(m)
                vertices_adj = self.adjt(m, heap_map)
                for v in vertices_adj:
                    menor_aresta = self.menor_aresta(v, m, EV_map)
                    heap_map[v] = self.MD[menor_aresta][-1]
                    if v not in EV_map.keys():
                        EV_map[v] = menor_aresta
                    else:
                        if self.MD[menor_aresta][-1] < self.MD[EV_map[v]][-1]:
                            EV_map[v] = menor_aresta
        dit = {}
        for a in EV_map.values():
            dit[a] = self.MD[a]
        return dit
    # FUNÇÕES

    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''

        # Dá o espaçamento correto de acordo com o tamanho do string do maior vértice
        espaco = ' '*(self.__maior_vertice)

        grafo_str = espaco + ' '

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca o espaço se não for o último vértice
                grafo_str += ' '

        grafo_str += '\n'

        for l in range(len(self.M)):
            grafo_str += self.N[l] + ' '
            for c in range(len(self.M)):
                grafo_str += str(self.M[l][c]) + ' '
            grafo_str += '\n'

        return grafo_str
