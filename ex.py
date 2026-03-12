"""
insert_beginning(value) — inserir elemento no início da lista - OK
insert_end(value) — inserir elemento no final da lista - OK
remove(value) — remover um elemento da lista
search(value) — buscar um elemento na lista - OK
print_list() — imprimir os elementos da lista - OK
size() — retornar o tamanho da lista - OK
is_empty() — verificar se a lista está vazia - OK
"""

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0
        
    def insert_beginning(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self._size += 1
        
    def insert_end(self, value):
        if self.is_empty():
            self.head = Node(value)
        else:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(value)
        self._size += 1
        
    # def remove(self, value):
        
    def is_empty(self):
        return self._size == 0

    def search(self, value):
        pointer = self.head
        i = 0
        while (pointer):
            if pointer.value == value:
                return i
            pointer = pointer.next
            i = i + 1
        return None
    # ou raise ValueError ("O elemento não está na lista")

    def size(self):
        return self._size
    
    def print_list(self):
        pointer = self.head

        while (pointer):
            print(pointer.value, end = " -> ")
            pointer = pointer.next
        print("None")
        
    def remove(self, value):
        if self.head == None:
            raise ValueError("A lista está vazia")
        elif self.head.value == value:
            self.head = self.head.next
            self._size -= 1
        else:
            aux = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.value == value:
                    aux.next = pointer.next
                    pointer.next = None
                else:
                    aux = pointer
                    pointer = pointer.next
            return True
        raise ValueError("Valor não encontrado")
            
lista = LinkedList()

print("A lista está vazia?")
print(lista.is_empty())
print("")

lista.insert_end(7)
lista.insert_end(10)
lista.insert_end(15)

lista.insert_beginning(3)

lista.print_list()

print("Tamanho:", lista.size())

print("Posição do 10:", lista.search(10))
print("Posição do 100:", lista.search(100))