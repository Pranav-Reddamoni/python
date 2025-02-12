class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        # print("node value assigned")

class linked_list:
    def __init__(self):
        self.head=None

    def insertatend(self,data):
        # print("node class called")
        new_node=node(data)

        if self.head==None:
            # print("head:",self.head,"\n")
            self.head=new_node
        else:
            # print("head is not null:",self.head)
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=new_node
            # print("temp next address:",temp.next,"\n")

    def insertatbegin(self,data):
        # print("node class called")
        new_node=node(data)
        if self.head==None:
            self.head=new_node
            # print("head:",self.head,"\n")
        else:
            new_node.next=self.head
            self.head=new_node
            # print("head:",self.head,"\n")

    def insertatmiddle(self,pos,data):
        # print("node class called")
        new_node=node(data)
        temp=self.head
        while pos-1>0:
            temp=temp.next
            pos=pos-1
        new_node.next=temp.next
        temp.next=new_node

    def deleteatend(self):
        # print("node class called")
        if self.head==None:
            print("list is empty")
        elif self.head.next==None:
            self.head=None
        else:
            temp=self.head
            while temp.next.next!=None:
                temp=temp.next
            temp.next=None
            # print(" node deleted")

    def deletebegin(self):
        # print("node class called")
        if self.head==None:
            print("list is empty")
        elif self.head.next==None:
            self.head=None
        else:
            self.head=self.head.next
            # print(" node deleted")

    def deletepos(self,pos):
        if pos==1:
            self.head=self.head.next
        else:
            temp=self.head
            while pos-2:
                temp=temp.next
                pos=pos-1
            temp.next=temp.next.next

    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end="-->")
            # print(temp.next)
            temp=temp.next


ll=linked_list()
# print("first node--------------------")

ll.insertatend(1)
# print("second node-------------------")
ll.insertatend(2)
# print("third node--------------------")
ll.insertatend(3)
# print("fourth node-------------------")
ll.insertatmiddle(1,4)
# print("fifth node--------------------")
ll.insertatbegin(5)
ll.insertatend(6)


ll.display()
ll.deleteatend()
print("\n last node deleted")
ll.display()
ll.deletebegin()
print("\n first node deleted")
ll.display()
ll.deletepos(2)
print("\n")
ll.display()

