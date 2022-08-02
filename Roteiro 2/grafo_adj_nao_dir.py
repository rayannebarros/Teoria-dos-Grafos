# -*- coding: utf-8 -*-

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

    def __init__(self, V=None, M=None):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param V: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma matriz de adjacência que guarda as arestas do grafo. Cada entrada da matriz tem um inteiro que indica a quantidade de arestas que ligam aqueles vértices
        '''

        if V is None:
            V = list()
        if M is None:
            M = list()

        for v in V:
            if not (Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

        self.N = list(V)

        if not M:
            for k in range(len(V)):
                M.append(list())
                for l in range(len(V)):
                    if k > l:
                        M[k].append('-')
                    else:
                        M[k].append(0)

        if len(M) != len(V):
            raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for c in M:
            if len(c) != len(V):
                raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for i in range(len(V)):
            for j in range(len(V)):
                '''
                Verifica se os índices passados como parâmetro representam um elemento da matriz abaixo da diagonal principal.
                Além disso, verifica se o referido elemento é um traço "-". Isso indica que a matriz é não direcionada e foi construída corretamente.
                '''
                if i > j and not (M[i][j] == '-'):
                    raise MatrizInvalidaException('A matriz não representa uma matriz não direcionada')

                aresta = V[i] + Grafo.SEPARADOR_ARESTA + V[j]
                if not (self.arestaValida(aresta)):
                    raise ArestaInvalidaException('A aresta ' + aresta + ' é inválida')

        self.M = list(M)

    def arestaValida(self, aresta=''):
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

        if not (self.existeVertice(aresta[:i_traco])) or not (self.existeVertice(aresta[i_traco + 1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def __primeiro_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o vértice X
        :param a: a aresta a ser analisada
        :return: O primeiro vértice da aresta
        '''
        return a[0:a.index(Grafo.SEPARADOR_ARESTA)]

    def __segundo_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o vértice Y
        :param a: A aresta a ser analisada
        :return: O segundo vértice da aresta
        '''
        return a[a.index(Grafo.SEPARADOR_ARESTA) + 1:]

    def __indice_primeiro_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o índice do vértice X na lista de vértices
        :param a: A aresta a ser analisada
        :return: O índice do primeiro vértice da aresta na lista de vértices
        '''
        return self.N.index(self.__primeiro_vertice_aresta(a))

    def __indice_segundo_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o índice do vértice Y na lista de vértices
        :param a: A aresta a ser analisada
        :return: O índice do segundo vértice da aresta na lista de vértices
        '''
        return self.N.index(self.__segundo_vertice_aresta(a))

    def existeAresta(self, a: str):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.arestaValida(self, a):
            for i in range(len(self.M)):
                for j in range(len(self.M)):
                    if self.M[self.__indice_primeiro_vertice_aresta(a)][self.__indice_segundo_vertice_aresta(a)]:
                        existe = True

        return existe

    def adicionaVertice(self, v):
        '''
        Inclui um vértice no grafo se ele estiver no formato correto.
        :param v: O vértice a ser incluído no grafo.
        :raises VerticeInvalidoException se o vértice já existe ou se ele não estiver no formato válido.
        '''
        if v in self.N:
            raise VerticeInvalidoException('O vértice {} já existe'.format(v))

        if self.verticeValido(v):
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

            self.N.append(v)  # Adiciona vértice na lista de vértices
            self.M.append([])  # Adiciona a linha

            for k in range(len(self.N)):
                if k != len(self.N) - 1:
                    self.M[k].append(0)  # adiciona os elementos da coluna do vértice
                    self.M[self.N.index(v)].append('-')  # adiciona os elementos da linha do vértice
                else:
                    self.M[self.N.index(v)].append(0)  # adiciona um zero no último elemento da linha
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, a):
        '''
        Adiciona uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''
        if self.arestaValida(a):
            i_a1 = self.__indice_primeiro_vertice_aresta(a)
            i_a2 = self.__indice_segundo_vertice_aresta(a)
            if i_a1 < i_a2:
                self.M[i_a1][i_a2] += 1
            else:
                self.M[i_a2][i_a1] += 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    def remove_aresta(self, a):
        '''
        Remove uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''
        if self.arestaValida(a):
            if self.existeAresta(a):
                i_a1 = self.__indice_primeiro_vertice_aresta(a)
                i_a2 = self.__indice_segundo_vertice_aresta(a)
                if i_a1 < i_a2:
                    self.M[i_a1][i_a2] -= 1
                else:
                    self.M[i_a2][i_a1] -= 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    def vertices_nao_adjacentes(self):
        vertex = []
        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if type(self.M[i][j]) is int:
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
                if type(self.M[i][j]) is int:
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
                if type(self.M[i][j]) is int:
                    if self.M[i][j] > 1:
                        return True
        return False

    def arestas_sobre_vertice(self, vertex):
        position = self.N.index(vertex)
        edges = []
        for i in range(len(self.M)):
            if type(self.M[position][i]) is int:
                if self.M[position][i] > 0:
                    for j in range(self.M[position][i]):
                        edges.append(self.N[position] + self.SEPARADOR_ARESTA + self.N[i])
        for i in range(len(self.M)):
            if type(self.M[i][position]) is int:
                if self.M[i][position] > 0:
                    for j in range(self.M[i][position]):
                        edges.append(self.N[i] + self.SEPARADOR_ARESTA + self.N[position])
        return edges

    def eh_completo(self):
        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if type(self.M[i][j]) is int and i != j and self.M[i][j] < 1:
                    return False
        return True

    def ha_ciclo(self):
        is_ciclic = self.search_for_cycle()
        edges_identifier = 1
        if is_ciclic:
            way = []
            start = is_ciclic[-1].split(self.SEPARADOR_ARESTA)[1]
            for i in range(len(is_ciclic) - 1, -1, -1):
                vertex = is_ciclic[i].split(self.SEPARADOR_ARESTA)
                if vertex[0] == start:
                    way.append(vertex[1] + self.SEPARADOR_ARESTA + vertex[0])
                    way.append('e' + str(edges_identifier))
                    return way
                way.append(vertex[1] + self.SEPARADOR_ARESTA + vertex[0])
                way.append('e' + str(edges_identifier))
                edges_identifier += 1
        return False

    def search_for_cycle(self, vertex=None, visited=None, way=None, edges=None):
        if vertex is None:
            vertex = self.N[0]
        if visited is None:
            visited = []
        if way is None:
            way = []
        if edges is None:
            edges = []
            for i in range(len(self.N)):
                for j in range(len(self.N)):
                    if type(self.M[i][j]) is int:
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

    def caminho_de_comprimento_n(self, n, vertex=None, visited=None, way=None, edges=None, counter=0):
        if n == 0:
            return False
        if way is None:
            way = []
        if vertex is None:
            vertex = self.N[0]
        if visited is None:
            visited = []
        if way is None:
            way = []
        if edges is None:
            edges = []
            for i in range(len(self.N)):
                for j in range(len(self.N)):
                    if type(self.M[i][j]) is int:
                        if self.M[i][j] > 0:
                            for k in range(self.M[i][j]):
                                edges.append(self.N[i] + self.SEPARADOR_ARESTA + self.N[j])
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
                    if self.caminho_de_comprimento_n(n, next[1], visited, way, edges, counter):
                        return True
                    else:
                        way.pop()
                        counter -= 1
                else:
                    if len(edges_adjacents) != 1:
                        way.append(vertex + self.SEPARADOR_ARESTA + next[0])
                        if self.caminho_de_comprimento_n(n, next[0], visited, way, edges, counter):
                            return True
                        else:
                            way.pop()
                            counter -= 1
        return False

    def eh_conexo(self, vertex=None, visited=None, way=None, edges=None):
        if way is None:
            way = []
        if visited is None:
            visited = []
        if len(self.N) == 1:
            return True
        if vertex is None:
            vertex = self.N[0]
        if edges is None:
            edges = []
            for i in range(len(self.N)):
                for j in range(len(self.N)):
                    if type(self.M[i][j]) is int:
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
                    if self.eh_conexo(next[1], visited, way, edges):
                        return True
                    else:
                        way.pop()
                else:
                    if len(edges_adjacently) != 1:
                        way.append(vertex + self.SEPARADOR_ARESTA + next[0])
                        if self.eh_conexo(next[0], visited, way, edges):
                            return True
                        else:
                            way.pop()
        return False

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
