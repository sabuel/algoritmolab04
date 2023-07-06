from estrutura_elementar import estrutura_elementar


class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def set_proximo(self, no):
        self.proximo = no

    def get_proximo(self):
        return self.proximo


class LinkedList(estrutura_elementar):
    def __init__(self):
        self.inicio = None

    def inserir_inicio(self, valor):
        if self.inicio is None:
            self.inicio = No(valor)
        else:
            novoNo = No(valor)
            novoNo.set_proximo(self.inicio)
            self.inicio = novoNo

    def inserir_fim(self, valor):
        if self.inicio is None:
            self.inicio = No(valor)
        else:
            novoNo = No(valor)
            aux = self.inicio
            while aux.get_proximo() is not None:
                aux = aux.get_proximo()
            aux.set_proximo(novoNo)

    def esta_vazio(self) -> bool:
        return self.inicio is None

    def remove(self, item):
        if self.esta_vazio():
            return
        
        if (self.inicio.valor == item):
            self.inicio = self.inicio.get_proximo()
            return
        
        atual = self.inicio
        while atual:
            if (atual.get_proximo().valor == item):
                proximo = atual.get_proximo()
                atual.set_proximo(proximo.get_proximo())
                return
            atual = atual.get_proximo()
    
    def remove_indice(self, index):
        if ((index < 0) or (index >= self.tamanho())):
            return

        if (index == 0):
            self.inicio = self.inicio.get_proximo()
            return
        
        atual = self.inicio
        indice = 0

        while atual:
            if (index == indice+1):
                proximo = atual.get_proximo()
                atual.set_proximo(proximo.get_proximo())
                return
                
            
            indice+=1
            atual = atual.get_proximo()


    def tamanho(self) -> int:
        tamanho = 0
        atual = self.inicio
        while atual:
            tamanho += 1
            atual = atual.get_proximo()
        return tamanho



    def limpa(self):
        self.inicio = None

    def procura(self, item) -> bool:
        if self.esta_vazio():
            return False
        atual = self.inicio
        while atual:
            if (atual.valor == item):
                return True
            atual = atual.get_proximo()
        return False

    def indice_de(self, item):
        indice = 0
        atual = self.inicio
        while atual:
            if (atual.valor == item):
                return indice
            indice += 1
            atual = atual.get_proximo()
        return -1


    def recupera_indice(self, index):
        if index < 0:
            return None
        
        atual = self.inicio
        indice = 0
        
        while atual:
            if (indice == index):
                return atual.valor
            indice += 1
            atual = atual.get_proximo()
        
        return None

