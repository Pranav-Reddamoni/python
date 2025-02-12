class Node:
    def __init__(self, data,prev):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insertatend(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        temp=self.head
        while temp.next:
            temp=temp.next
            newNode.prev=temp

    def display(self):
        if not temp:
            print("Empty list")
        while temp:
            print(temp.data,end="<-->")
            temp=temp.next

dll=DoublyLinkedList()
dll.insertatend(1)
dll.insertatend(2)
dll.insertatend(3)
dll.insertatend(4)
dll.display()