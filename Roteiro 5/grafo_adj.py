# -*- coding: utf-8 -*-

from copy import deepcopy

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
        for v in N:
            if not (Grafo.vertice_valido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

        self.N = N

        if len(M) != len(N):
            raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for c in M:
            if len(c) != len(N):
                raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for i in range(len(N)):
            for j in range(len(N)):
                aresta = N[i] + Grafo.SEPARADOR_ARESTA + N[j]
                if not (self.aresta_valida(aresta)):
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

        if not (self.existe_vertice(aresta[:i_traco])) or not (self.existe_vertice(aresta[i_traco + 1:])):
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
        return a[a.index(Grafo.SEPARADOR_ARESTA) + 1:]

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
                if k != len(self.N) - 1:
                    self.M[k].append(0)
                self.M[self.N.index(v)].append(0)
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adiciona_aresta(self, a):
        if self.aresta_valida(a):
            self.M[self.indice_primeiro_vertice_aresta(a)][self.indice_segundo_vertice_aresta(a)] += 1
        else:
            ArestaInvalidaException('A aresta ' + self.A[a] + ' é inválida')

    def vertices_nao_adjacentes(self):
        vertex = []
        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if self.M[i][j] == 0:
                    vertex.append(self.N[i] + self.SEPARADOR_ARESTA + self.N[j])
        return vertex

    def ha_laco(self):
        for i in range(len(self.N)):
            if self.M[i][i] > 0:
                return True
        return False

    def grau(self, vertex):
        degree = 0
        way = []
        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if self.M[i][j] > 0:
                    for k in range(self.M[i][j]):
                        way.append(self.N[i] + self.SEPARADOR_ARESTA + self.N[j])
        for e in way:
            if vertex in e:
                degree += 1
        return degree

    def ha_paralelas(self):
        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if self.M[i][j] > 1:
                    return True
        return False

    def arestas_sobre_vertice(self, vertex):
        position = self.N.index(vertex)
        edges = []
        for i in range(len(self.M)):
            if self.M[position][i] > 0:
                for j in range(self.M[position][i]):
                    edges.append(self.N[position] + self.SEPARADOR_ARESTA + self.N[i])
        for i in range(len(self.M)):
            if self.M[i][position] > 0:
                for j in range(self.M[i][position]):
                    edges.append(self.N[i] + self.SEPARADOR_ARESTA + self.N[position])
        return edges

    def arestas_partindo_do_vertice(self, vertice):
        way = []
        final = []
        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if self.M[i][j] > 0:
                    for k in range(self.M[i][j]):
                        way.append(self.N[i] + self.SEPARADOR_ARESTA + self.N[j])
        for i in way:
            proximo = i.split(self.SEPARADOR_ARESTA)
            if proximo[0] == vertice:
                final.append(proximo[0] + self.SEPARADOR_ARESTA + proximo[1])
        return final

    def eh_completo(self):
        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if i != j and self.M[i][j] < 1:
                    return False
        return True

    def ha_ciclo(self):
        is_ciclic = self.search_for_cycle()
        edges_identifier = 1
        if is_ciclic != False:
            way = []
            start = is_ciclic[-1].split(self.SEPARADOR_ARESTA)[1]
            for i in range(len(is_ciclic) - 1, -1, -1):
                vertex = is_ciclic[i].split(self.SEPARADOR_ARESTA)
                if vertex[0] == start:
                    way.append(vertex[1] + self.SEPARADOR_ARESTA + vertex[0])
                    return way
                way.append(vertex[1] + self.SEPARADOR_ARESTA + vertex[0])
                edges_identifier += 1
        return False

    def search_for_cycle(self, vertex=None, visited=None, way=None, edges=None):
        if visited is None:
            visited = list()
        if way is None:
            way = list()
        if vertex == None:
            vertex = self.N[0]
        if edges == None:
            edges = []
            for i in range(len(self.N)):
                for j in range(len(self.N)):
                    if self.M[i][j] > 0:
                        for k in range(self.M[i][j]):
                            edges.append(self.N[i] + self.SEPARADOR_ARESTA + self.N[j])
        if vertex in visited:
            return way
        else:
            visited.append(vertex)
            edges_adjacents = self.arestas_sobre_vertice(vertex)
            for i in edges_adjacents:
                if i in edges:
                    edges.remove(i)
                next = i.split(self.SEPARADOR_ARESTA)
                if next[0] == vertex:
                    way.append(vertex + self.SEPARADOR_ARESTA + next[1])
                    result = self.search_for_cycle(next[1], visited, way, edges)
                    if result != False:
                        return result
                    else:
                        way.pop()
                else:
                    if len(edges_adjacents) != 1:
                        way.append(vertex + self.SEPARADOR_ARESTA + next[0])
                        result = self.search_for_cycle(next[0], visited, way, edges)
                        if result != False:
                            return result
                        else:
                            way.pop()
        return False

    def caminho_de_comprimento_n(self, n, vertex=None, visited=None, way=None, edges=None, counter=None):
        if counter is None:
            counter = 0
        if vertex is None:
            vertex = self.N[0]
        if visited is None:
            visited = list()
        if edges is None:
            edges = []
            for i in range(len(self.N)):
                for j in range(len(self.N)):
                    if self.M[i][j] > 0:
                        for k in range(self.M[i][j]):
                            edges.append(self.N[i] + self.SEPARADOR_ARESTA + self.N[j])
        if way is None:
            way = list()
        if vertex in visited:
            return False
        else:
            counter += 1
            if counter == n:
                return True
            visited.append(vertex)
            edges_adjacents = self.arestas_sobre_vertice(vertex)
            for i in edges_adjacents:
                if i in edges:
                    edges.remove(i)
                next = i.split(self.SEPARADOR_ARESTA)
                if next[0] == vertex:
                    way.append(vertex + self.SEPARADOR_ARESTA + next[1])
                    result = self.caminho_de_comprimento_n(n, next[1], visited, way, edges, counter)
                    if result:
                        return True
                    else:
                        way.pop()
                        counter -= 1
                else:
                    if len(edges_adjacents) != 1:
                        way.append(vertex + self.SEPARADOR_ARESTA + next[0])
                        result = self.caminho_de_comprimento_n(n, next[0], visited, way, edges, counter)
                        if result:
                            return True
                        else:
                            way.pop()
                            counter -= 1
        return False

    def conexo(self, vertex=None, visited=None, way=None, edges=None):
        if visited is None:
            visited = []
        if way is None:
            way = []
        if vertex is None:
            vertex = self.N[0]
        if edges is None:
            edges = []
            for i in range(len(self.N)):
                for j in range(len(self.N)):
                    if self.M[i][j] > 0:
                        for k in range(self.M[i][j]):
                            edges.append(self.N[i] + self.SEPARADOR_ARESTA + self.N[j])
        if vertex in visited:
            if len(visited) == len(self.N):
                return True
            else:
                return False
        else:
            visited.append(vertex)
            edges_adjacently = self.arestas_sobre_vertice(vertex)
            for i in edges_adjacently:
                next = i.split(self.SEPARADOR_ARESTA)
                if next[0] == vertex:
                    way.append(vertex + self.SEPARADOR_ARESTA + next[1])
                    if self.conexo(next[1], visited, way, edges):
                        return True
                    else:
                        way.pop()
                else:
                    if len(edges_adjacently) != 1:
                        way.append(vertex + self.SEPARADOR_ARESTA + next[0])
                        if self.conexo(next[0], visited, way, edges):
                            return True
                        else:
                            way.pop()
        return False

    def caminho_euleriano(self):
        degree = 0
        vertice_v = []
        if self.conexo():
            if self.ha_ciclo():
                vertex = self.N
                for i in vertex:
                    if self.grau(i) % 2 != 0:
                        degree += 1
                        vertice_v.append(self.grau(i))
                if degree == 0:
                    return True
                if len(vertice_v) == 2:
                    return True
        return False

    def procura_caminho(self, vertex=None, way=None, edges=None):
        if self.caminho_euleriano():
            if way is None:
                way = list()
            if vertex == None:
                vertex = self.N[0]
            if edges == None:
                edges = []
                for i in range(len(self.N)):
                    for j in range(len(self.N)):
                        if self.M[i][j] > 0:
                            for k in range(self.M[i][j]):
                                edges.append(self.N[i] + self.SEPARADOR_ARESTA + self.N[j])
            if len(edges) == 0:
                return way
            else:
                edges_adjacents = self.arestas_sobre_vertice(vertex)
                for i in edges_adjacents:
                    if i in edges:
                        for j in range(edges.count(i)):
                            edges.remove(i)
                    next = i.split(self.SEPARADOR_ARESTA)
                    if next[0] == vertex:
                        ars = (vertex + self.SEPARADOR_ARESTA + next[1])
                        if ars not in way and ars[::-1] not in way:
                            way.append(vertex + self.SEPARADOR_ARESTA + next[1])
                            result = self.procura_caminho(next[1], way, edges)
                            if result != False:
                                return result
                            else:
                                if len(edges) == 0:
                                    return way
                                way.pop()
                        else:
                            continue
                    else:
                        if len(edges_adjacents) != 1:
                            ars = (vertex + self.SEPARADOR_ARESTA + next[0])
                            if ars not in way and ars[::-1] not in way:
                                way.append(vertex + self.SEPARADOR_ARESTA + next[0])
                                result = self.procura_caminho(next[0], way, edges)
                                if result != False:
                                    return result
                                else:
                                    if len(edges) == 0:
                                        return way
                                    way.pop()
                            else:
                                continue
        return False

    def aresta_com_peso(self):
        edges = []
        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if self.M[i][j] > 0:
                    for k in range(self.M[i][j]):
                        edges.append(self.N[i] + self.SEPARADOR_ARESTA + self.N[j])
        arestas = {}
        for i in edges:
            arestas[i] = 1
        return arestas

    def warshall(self):
        e = deepcopy(self.M)
        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if e[j][i] != 0:
                    for k in range(len(self.N)):
                        e[j][k] = max(e[j][k], e[i][k])
                        if e[j][k] > 1:
                            e[j][k] = 1
        return e

    def dijkstra(self, vertices, arestas, u, v, carga, p_recarga):
        result = self.dijkstraLoad(vertices, arestas, u, v, carga, p_recarga)
        if result is None:
            return False
        else:
            final = ''
            for i in result:
                final += i
                if i == result[-1]:
                    break
                final += ' --> '
            return final

    def dijkstra_mod(self, vertices, arestas, u, v):
        beta = {}
        phi = {}
        pi = {}

        # PASSO 2:
        for i in range(len(vertices)):
            beta[vertices[i]] = float('inf')
            phi[vertices[i]] = 0
            pi[vertices[i]] = 0

        # PASSO 1:
        beta[u] = 0
        phi[u] = 1
        pi[u] = "-"
        w = u

        verificacao = 0
        while (w != v):
            # PASSO 3:
            verificacao2 = 0
            for ligacoes in arestas:
                if (ligacoes[0] == w):
                    if phi[ligacoes[2]] == 0 and beta[ligacoes[2]] > beta[w] + arestas[ligacoes]:
                        beta[ligacoes[2]] = beta[w] + arestas[ligacoes]
                        pi[ligacoes[2]] = w
                        verificacao2 += 1

            # PASSO 4:
            minimoBeta = float('inf')
            for vertice in vertices:
                if phi[vertice] == 0 and beta[vertice] < float('inf'):
                    if beta[vertice] < minimoBeta:
                        minimoBeta = beta[vertice]

            if verificacao2 == 0 and minimoBeta == float('inf'):
                verificacao += 1
                break

            for vertice in vertices:
                if beta[vertice] == minimoBeta and phi[vertice] == 0 and beta[vertice] < float('inf'):
                    phi[vertice] = 1
                    w = vertice
                    break

        if verificacao == 1:
            return False

        else:
            # PEGANDO OS ANTECESSORES
            atual = v
            lista = []
            while atual != u:
                for aaa in pi:
                    if aaa == atual:
                        lista.append(atual)
                        atual = pi[atual]
                        break

            lista.append(atual)

            return len(lista) - 1, lista[::-1]


    def dijkstraLoad(self, vertices, arestas, u, v, carga, pontosRecarga):
        inicial = u
        pontosRecarga.insert(0, u)
        pontosRecarga.append(v)

        possibilidades = {}

        for i in range(len(pontosRecarga)):
            for j in range(len(pontosRecarga)):
                if u == pontosRecarga[j] or self.dijkstra_mod(vertices, arestas, u, pontosRecarga[j]) == False:
                    continue
                caminho = self.dijkstra_mod(vertices, arestas, u, pontosRecarga[j])[0]
                if caminho <= carga:
                    possibilidades[u + "-" + pontosRecarga[j]] = caminho
            u = pontosRecarga[i]
            if i > 0:
                carga = 5

        lista = self.dijkstra_mod(pontosRecarga, possibilidades, inicial, v)

        if lista == False:
            return None

        caminhoFinal = []
        for i in range(len(lista[1]) - 1):
            caminhoFinal.append(self.dijkstra_mod(vertices, arestas, lista[1][i], lista[1][i + 1])[1])

        Final = []

        for i in range(len(caminhoFinal)):
            for j in range(len(caminhoFinal[i])):
                if (caminhoFinal[i][j] not in Final):
                    Final.append(caminhoFinal[i][j])

        return Final

    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''

        # Dá o espaçamento correto de acordo com o tamanho do string do maior vértice
        espaco = ' ' * (self.__maior_vertice)

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
