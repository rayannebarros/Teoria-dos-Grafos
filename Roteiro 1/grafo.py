
'''
Nome: Micael Marques Rodrigues Silva
Nome: Rayanne Kelly Marcelino Barros Elias
'''
class VerticeInvalidoException(Exception):
    pass


class ArestaInvalidaException(Exception):
    pass


class Grafo:
    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'

    def __init__(self, N=[], A={}):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param N: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma dicionário que guarda as arestas do grafo.
            A chave representa o nome da aresta e o valor é uma string que contém dois vértices separados por um traço.
        '''
        for v in N:
            if not (Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

        self.N = N

        for a in A:
            if not (self.arestaValida(A[a])):
                raise ArestaInvalidaException('A aresta ' + A[a] + ' é inválida')

        self.A = A

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

        # Verifica se as arestas antes de depois do elemento separador existem no Grafo
        if not (self.existeVertice(aresta[:i_traco])) or not (self.existeVertice(aresta[i_traco + 1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def __arestas(self, vertice, arestas=None):
        if arestas == None:
            arestas = self.A.values()
        return filter(lambda v: v.startswith(vertice) or v.endswith(vertice), arestas)

    def existeVertice(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def existeAresta(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.arestaValida(self, aresta):
            for k in self.A:
                if aresta == self.A[k]:
                    existe = True

        return existe

    def adicionaVertice(self, v):
        '''
        Adiciona um vértice no Grafo caso o vértice seja válido e não exista outro vértice com o mesmo nome
        :param v: O vértice a ser adicionado
        :raises: VerticeInvalidoException se o vértice passado como parâmetro não puder ser adicionado
        '''
        if self.verticeValido(v) and not self.existeVertice(v):
            self.N.append(v)
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, nome, a):
        '''
        Adiciona uma aresta no Grafo caso a aresta seja válida e não exista outra aresta com o mesmo nome
        :param v: A aresta a ser adicionada
        :raises: ArestaInvalidaException se a aresta passada como parâmetro não puder ser adicionada
        '''
        if self.arestaValida(a):
            self.A[nome] = a
        else:
            ArestaInvalidaException('A aresta ' + self.A[a] + ' é inválida')

    # letra a
    def vertices_nao_adjacentes(self):
        lista = []
        for i in self.N:  # i são todos os vertices
            for j in self.N:  # j também são todos os vertices
                aresta1 = i + self.SEPARADOR_ARESTA + j
                aresta2 = j + self.SEPARADOR_ARESTA + i
                if aresta1 not in self.A.values() and aresta2 not in self.A.values():
                    lista.append(aresta1)
        return lista

    # letra b
    def ha_laco(self):
        for i in self.A.values():
            vertices = i.split(self.SEPARADOR_ARESTA)
            if vertices[0] == vertices[1]:
                return True
        return False

    # letra c
    def ha_paralelas(self):
        for i in self.N:
            for j in self.N:
                cont = 0
                aresta = i + self.SEPARADOR_ARESTA + j
                for k in self.A.values():
                    if aresta in k:
                        cont += 1
                        if cont > 1:
                            return True
        return False

    # letra d
    def grau(self, vertice):
        count = 0
        for a in self.A.values():
            if vertice in a:
                count += 1
        return count

    # letra e
    def arestas_sobre_vertice(self, vertice):
        lista = []
        for i in self.A.keys():
            aresta = self.A.get(i)
            if vertice in aresta:
                lista.append(i)
        return lista

    # letra f
    def eh_completo(self):
        caminho = list(self.A.values())
        vertex = self.N
        ligacoes = []
        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if i != j:
                    comb = vertex[i] + self.SEPARADOR_ARESTA + vertex[j]
                    if comb[::-1] not in ligacoes:
                        ligacoes.append(comb)
        for i in range(len(ligacoes)):
            if ligacoes[i] not in caminho and ligacoes[i][::-1] not in caminho:
                return False
        return True

    # desafios
    # letra g
    def ha_ciclo(self):
        res = self.__procurar_ciclo()
        if res != False:
            caminho = []
            inicio = res[-1].split(self.SEPARADOR_ARESTA)[1]
            for i in range(len(res) - 1, -1, -1):
                vertices = res[i].split(self.SEPARADOR_ARESTA)
                if vertices[0] == inicio:
                    caminho.append(vertices[1] + self.SEPARADOR_ARESTA + vertices[0])
                    return caminho
                caminho.append(vertices[1] + self.SEPARADOR_ARESTA + vertices[0])
        return False

    def __procurar_ciclo(self, vertice=None, visitados=[], caminho=[], arestas=None):
        if vertice == None:
            vertice = self.N[0]
        if arestas == None:
            arestas = list(self.A.values())
        if vertice in visitados:
            return caminho
        else:
            visitados.append(vertice)
            a = list(self.__arestas(vertice, arestas))
            for i in a:
                arestas.remove(i)
                proximo = i.split(self.SEPARADOR_ARESTA)
                if proximo[0] == vertice:
                    caminho.append(vertice + self.SEPARADOR_ARESTA + proximo[1])
                    resultado = self.__procurar_ciclo(proximo[1], visitados, caminho, arestas)
                    if resultado != False:
                        return resultado
                    else:
                        caminho.pop()
                else:
                    caminho.append(vertice + self.SEPARADOR_ARESTA + proximo[0])
                    resultado = self.__procurar_ciclo(proximo[0], visitados, caminho, arestas)
                    if resultado != False:
                        return resultado
                    else:
                        caminho.pop()
        return False

    # letra h
    def comprimento_de_tamanho_n(self, n, vertice=None, visitados=[], caminho=[], arestas=None, c=0):
        if vertice == None:
            vertice = self.N[0]
        if arestas == None:
            arestas = list(self.A.values())
        if vertice in visitados:
            return False
        else:
            c += 1
            if c == n:
                return True
            visitados.append(vertice)
            a = list(self.__arestas(vertice, arestas))
            for i in a:
                if i in arestas:
                    arestas.remove(i)
                proximo = i.split(self.SEPARADOR_ARESTA)
                if proximo[0] == vertice:
                    caminho.append(vertice + self.SEPARADOR_ARESTA + proximo[1])
                    resultado = self.comprimento_de_tamanho_n(n, proximo[1], visitados, caminho, arestas, c)
                    if resultado != False:
                        return True
                    else:
                        caminho.pop()
                        c -= 1
                else:
                    caminho.append(vertice + self.SEPARADOR_ARESTA + proximo[0])
                    resultado = self.comprimento_de_tamanho_n(n, proximo[0], visitados, caminho, arestas, c)
                    if resultado != False:
                        return True
                    else:
                        caminho.pop()
                        c -= 1
        return False

    #letra i
    def eh_conexo(self, v=None):
        if v == None:
            self.lis_path = []
            self.lis_a_percoridas = []
            self.vertice = self.N[0]
            self.lis_path.append(self.vertice)
            self.eh_conexo(v=self.vertice)
        else:
            vertice_reccebido = v
            lis_a = []
            for a in sorted(self.A):
                let = self.A[a].split(Grafo.SEPARADOR_ARESTA)
                if vertice_reccebido in let:
                    let.remove(vertice_reccebido)
                    let = let[0]
                    if a not in self.lis_a_percoridas and let != vertice_reccebido:
                        lis_a.append(a)
                        self.lis_a_percoridas.append(a)
            for a1 in lis_a:
                let1 = self.A[a1].split(Grafo.SEPARADOR_ARESTA)
                let1.remove(vertice_reccebido)
                let1 = let1[0]
                if let1 not in self.lis_path:
                    self.lis_path.append(let1)
                    self.eh_conexo(v=let1)
        if len(self.lis_path) == len(self.N):
            return True
        else:
            return False
        #desafios


    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''
        grafo_str = ''

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca a vírgula se não for o último vértice
                grafo_str += ", "

        grafo_str += '\n'

        for i, a in enumerate(self.A):
            grafo_str += self.A[a]
            if not (i == len(self.A) - 1):  # Só coloca a vírgula se não for a última aresta
                grafo_str += ", "

        return grafo_str
