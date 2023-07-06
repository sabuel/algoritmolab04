from lista_ligada import LinkedList

class pilhas():
    def __init__(self):
        self.lista = LinkedList

    def esta_vazia(self):
        return self.lista.esta_vazio()

    def tamanho(self):
        return self.lista.tamanho()

    def push(self, item):
        self.lista.inserir_inicio(item)

    def pop(self) -> int:
        if self.esta_vazia():
            return
        valor = self.lista.inicio.valor
        self.lista.remove(valor)
        return valor
    
    def search(self, item):
        return self.lista.procura(item)
            