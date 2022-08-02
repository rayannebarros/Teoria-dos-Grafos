# -*- coding: utf-8 -*-

class VerticeInvalidoException(Exception):
    pass

class ArestaInvalidaException(Exception):
    pass

class MatrizInvalidaException(Exception):
    pass

class Grafo2:

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

        if V == None:
            V = list()
        if M == None:
            M = list()

        for v in V:
            if not(Grafo2.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

        self.N = list(V)

        if M == []:
            for k in range(len(V)):
                M.append(list())
                for l in range(len(V)):
                    if k>l:
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
                if i>j and not(M[i][j] == '-'):
                    raise MatrizInvalidaException('A matriz não representa uma matriz não direcionada')


                aresta = V[i] + Grafo2.SEPARADOR_ARESTA + V[j]
                if not(self.arestaValida(aresta)):
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
        if aresta.count(Grafo2.SEPARADOR_ARESTA) != Grafo2.QTDE_MAX_SEPARADOR:
            return False

        # Índice do elemento separador
        i_traco = aresta.index(Grafo2.SEPARADOR_ARESTA)

        # O caractere separador não pode ser o primeiro ou o último caractere da aresta
        if i_traco == 0 or aresta[-1] == Grafo2.SEPARADOR_ARESTA:
            return False

        if not(self.existeVertice(aresta[:i_traco])) or not(self.existeVertice(aresta[i_traco+1:])):
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
        return vertice != '' and vertice.count(Grafo2.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo2.verticeValido(vertice) and self.N.count(vertice) > 0

    def __primeiro_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o vértice X
        :param a: a aresta a ser analisada
        :return: O primeiro vértice da aresta
        '''
        return a[0:a.index(Grafo2.SEPARADOR_ARESTA)]

    def __segundo_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o vértice Y
        :param a: A aresta a ser analisada
        :return: O segundo vértice da aresta
        '''
        return a[a.index(Grafo2.SEPARADOR_ARESTA)+1:]

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
        if Grafo2.arestaValida(self, a):
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

            self.N.append(v) # Adiciona vértice na lista de vértices
            self.M.append([]) # Adiciona a linha

            for k in range(len(self.N)):
                if k != len(self.N) -1:
                    self.M[k].append(0) # adiciona os elementos da coluna do vértice
                    self.M[self.N.index(v)].append('-') # adiciona os elementos da linha do vértice
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
        lista=[]
        for i in range(len(self.M)):
            for a in range(len(self.M)):
                if self.M[i][a]==0:
                    lista+=['{}-{}'.format(self.N[i],self.N[a])]
        return lista

    def ha_laco(self):
        for i in range(len(self.M)):
            if self.M[i][i] == 0:
                continue
            else:
                return True
        return False

    def ha_paralelas(self):
        for i in range(len(self.M)):
            for a in range(len(self.M)):
                if self.M[i][a] == 2:
                    return True
        return False

    def grau(self, v):
        posicao = self.N.index(v)
        cont = 0
        for i in range(len(self.M)):
            for a in range(len(self.M)):
                if (i == posicao or a == posicao) and self.M[i][a] != '-':
                    cont += self.M[i][a]
        return cont

    def arestas_sobre_vertice(self, v):
        posicao = self.N.index(v)
        lista = []
        for i in range(len(self.M)):
            for a in range(len(self.M)):
                if (i == posicao or a == posicao) and (self.M[i][a] == 1 or self.M[i][a] == 2):
                    for j in range(self.M[i][a]):
                        lista += ['{}-{}'.format(self.N[i], self.N[a])]

        return lista

    def completo(self):
        for i in range(len(self.M)):
            for a in range(len(self.M)):
                if self.M[i][a] == 0 and i != a:
                    return False
        return True

    def conexo(self):
        aresta = self.M
        vertice = self.N
        conexo = 0
        for i in range(len(vertice)):
            conti = True
            for a in range(len(aresta)):
                for v in range(len(aresta)):
                    if (a != v and v == i) and (aresta[a][v] != '-' and aresta[a][v] != 0) and conti == True:
                        conexo += 1
                        conti = False
        if conexo == len(vertice) - 1:
            return True
        else:
            return False

    def busca_prof_nao_dir(self):
        aresta = self.M
        vertices = self.N
        retorno=[]
        list_DFS=[]
        vez=vertices[0]
        lista1=[vez] #guarda os vertices verificados
        fim=False
        while fim==False:
            for i in range(len(vertices)):
                for a in range(len(vertices)):
                    if vertices[i]==vez and ((aresta[i][a]!='-' and aresta[i][a]!=0) or (aresta[a][i]!='-' and aresta[a][i]!=0)) and (vertices[a] in lista1)==False and (('{}-{}'.format(vertices[i],vertices[a]) in list_DFS)==False and ('{}-{}'.format(vertices[a],vertices[i]) in list_DFS)==False):
                        #verifica se é uma aresta valida(DFS)
                        lista1+=vertices[a]
                        vez=vertices[a]
                        list_DFS += ['{}-{}'.format(vertices[i], vertices[a])]
                    elif vertices[i] == vez and a == len(vertices) - 1: # caso seja o ultimo vertice da lista analisa se é de retorno e se precisa trocar a vez pro vértice anterior
                        if vertices[i]==vez and ((aresta[i][a]!='-' and aresta[i][a]!=0) or (aresta[a][i]!='-' and aresta[a][i]!=0)) and (vertices[a] in lista1)==True and (('{}-{}'.format(vertices[i],vertices[a]) in list_DFS)==False and ('{}-{}'.format(vertices[a],vertices[i]) in list_DFS)==False)and (('{}-{}'.format(vertices[i],vertices[a]) in retorno)==False and ('{}-{}'.format(vertices[a],vertices[i]) in retorno)==False):
                            retorno+= ['{}-{}'.format(vertices[i], vertices[a])]
                            vez = lista1[lista1.index(vertices[i]) - 1]
                        else:
                            vez = lista1[lista1.index(vertices[i]) - 1]
                    elif vertices[i]==vez and ((aresta[i][a]!='-' and aresta[i][a]!=0) or (aresta[a][i]!='-' and aresta[a][i]!=0)) and (vertices[a] in lista1)==True and (('{}-{}'.format(vertices[i],vertices[a]) in list_DFS)==False and ('{}-{}'.format(vertices[a],vertices[i]) in list_DFS)==False) and (('{}-{}'.format(vertices[i],vertices[a]) in retorno)==False and ('{}-{}'.format(vertices[a],vertices[i]) in retorno)==False):
                        #verifica se é de retorno
                        retorno+=['{}-{}'.format(vertices[i],vertices[a])]
                    elif vertices[i]==vez and vez==vertices[0] and len(lista1)==len(vertices): #verifica se todos os vertices já foram analisados
                        fim=True


        return list_DFS,retorno




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
