from node import Node
class Pilha():
    """Modelagem da Pilha"""

    def __init__(self):
        """Construtor"""
        self.top = None
        self.size = 0

    def __len__(self):
        """Tamanho da Pilha"""
        return self.size
    
    def __repr__(self):
        """Retorna uma representação da pilha"""
        t = ""
        ptr = self.top
        while(ptr):
            t= t + str(ptr.character)+ "\n"
            ptr = ptr.next
        return t

    def push(self, character):
        """Empilha um elemento"""
        new_node = Node(character)
        new_node.next = self.top
        self.top = new_node
        self.size = self.size + 1

    def pop(self):
        """Desempilha um elemento"""
        if self.size >0:
            node = self.top
            self.top = self.top.next
            self.size = self.size - 1
            return node
        raise IndexError("Empty Stack")

    def peek(self):
        """Retorna quem está no topo da pilha"""
        if self.top == None:
            return None
        else:
            return str(self.top.character)