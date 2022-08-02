# -*- coding: utf-8 -*-

'''
Micael Marques Rodrigues Silva
Rayanne Kelly Marcelino Barros Elias
'''

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

    def khan(self):
        edges = deepcopy(self.M) # Cria as arestas na forma de matriz
        vertex = self.N
        khan_way = []
        for i in range(len(vertex)):
            for j in range(len(vertex)):  # percorre a matriz procurando um vertice fonte
                if edges[j][i] > 0:  # caso tenha alguma aresta chegando nesse vertice pula pro proximo
                    break
                if j == len(vertex) - 1:  # caso tenha terminado de analisar e não achou nenhuma aresta é vertice fonte
                    khan_way += [vertex[i]]  # adiciona na lista
                    for k in range(len(vertex)):  # exclui as arestas que partem desse vertice
                        if edges[i][k] > 0:
                            edges[i][k] = 0
        return khan_way

    def dfs_recursion(self, v, vertex, edges):
        recursion_dfs = []
        index = vertex.index(v)  # guarda a posição do vertice pra não precisar fazer dois for
        for i in range(len(vertex)):  # percore buscando uma aresta que parte nesse vertice
            if edges[index][i] > 0:  # se achar envia de novo até achar um vertice sem arestas partindo dele (vertice sem filho)
                recursion_dfs += self.dfs_recursion(vertex[i], vertex, edges)  # adiciona na lista
                for j in range(len(vertex)):  # exclui todas as outras arestas que chegam nesse vertice, se não é adicionado de novo depois
                    if edges[j][i] > 0:
                        edges[j][i] = 0
            if i == len(vertex) - 1:  # caso seja um vertice sem filho adiciona na lista e retorna
                recursion_dfs += [vertex[index]]
                return recursion_dfs

    def dfs(self):
        edge_copying = deepcopy(self.M) #faz uma cópia do grafo porque vai modifica-lo
        edges=self.M #guarda o grafo original
        vertex = self.N
        list_dfs = list()
        for i in range(len(vertex)):
            for a in range(len(vertex)):#procura um vertice fonte
                if edges[a][i]>0: #se não for pula pro proximo
                    break
                elif a==len(vertex)-1: #caso tenha terminado é vertice fonte
                    for v in range(len(vertex)):# procura uma aresta que parte dele
                        if edge_copying[i][v] > 0:
                            list_dfs+=self.dfs_recursion(vertex[v],vertex,edge_copying) #envia o vertice ligado a ele para fazer a busca e adiciona na lista
                            for j in range(len(vertex)): #remove todas as outras arestas que chegam nesse outro vertice, se não ele é adicionado de novo depois
                                if edge_copying[j][v] > 0:
                                    edge_copying[j][v] = 0
                        if v==len(vertex)-1: #se terminou de analisar todas as arestas adiciona esse vertice na lista
                            list_dfs += [vertex[i]]
        list_dfs= list_dfs[::-1] #inverte a lista
        return list_dfs

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
