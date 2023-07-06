from lista_ligada import LinkedList

class filas():
    def __init__(self):
        self.lista = LinkedList
    
    def esta_vazia(self):
        return self.lista.esta_vazio()
    
    def enfila(self, item):
        self.lista.inserir_fim(item)
    
    def desenfila(self) -> int:
        if self.esta_vazia():
            return
        valor = self.lista.inicio.valor
        self.lista.remove(valor)
        return valor