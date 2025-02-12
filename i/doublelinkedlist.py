class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertatend(self,data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.prev = self.tail
            self.tail.next = newnode
            self.tail = newnode

    def display(self):
        current = self.head
        while current:
            print(current.data,end="<-->")
            current = current.next

dll = DoublyLinkedList()
dll.insertatend(1)
dll.insertatend(2)
dll.insertatend(3)
dll.insertatend(4)
dll.display()