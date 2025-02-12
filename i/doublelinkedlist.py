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

    def insertatbegin(self,data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode

    def insertatpos(self,pos,data):
        newnode = node(data)
        temp = self.head
        while pos-1 > 0:
            temp=temp.next
            pos=pos-1
        newnode.prev=temp
        newnode.next=temp.next
        temp.next.prev=newnode
        temp.next=newnode

    def deleteend(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.tail=self.tail.prev
            self.tail.next=None

    def deletebegin(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head=self.head.next
            self.head.prev=None

    def deletepos(self,pos):
        if pos==1:
            self.head=self.head.next
            self.head.prev=None
        else:
            temp=self.head
            while (pos-2 !=0):
                temp=temp.next
                pos=pos-1
            temp.next=temp.next.next
            temp.next.prev=temp

    def display(self):
        temp = self.head
        while temp!=None:
            print(temp.data,end="<-->")
            temp = temp.next

    def displayreverse(self):
        temp = self.tail
        while temp!=None:
            print(temp.data,end="<-->")
            temp = temp.prev

dll = DoublyLinkedList()
dll.insertatend(1)
dll.insertatend(2)
dll.insertatend(3)
dll.insertatend(4)
dll.insertatbegin(5)
dll.insertatpos(2,6)
dll.display()
print("\n\n")
dll.displayreverse()
print("\n")
dll.display()
dll.deleteend()
print("\n\n")
dll.display()
print("\n\n")
dll.displayreverse()
print("\n")
dll.deletebegin()
print("\n\n")
dll.display()
print("\n\n")
dll.displayreverse()
dll.deletepos(2)
print("\n\n")
dll.display()