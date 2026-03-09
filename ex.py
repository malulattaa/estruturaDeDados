class Node:
    def _init_(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None
        
    def insert_beginning(self, data) -> None:
        novo_node = Node(data)
        
        