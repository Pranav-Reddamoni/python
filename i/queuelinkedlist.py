class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,data):
        newnode=node(data)
        if self.front==None and self.rear==None:
            self.front=newnode
            self.rear=newnode
        else:
            self.rear.next=newnode
            self.rear=newnode
            # print("enqueue")

    def dequeue(self):
        if self.front==None:
            print("queue is empty")
        elif self.front==self.rear:
            print(self.front.data,"dequeued")
            self.front=self.rear=None
        else:
            print(self.front.data,"dequeued")
            self.front=self.front.next

    def display(self):
        if self.front==None:
            print("queue is empty")
        else:
            print("Queue is",end=" ")
            temp=self.front
            while temp:
                print(temp.data,end=" ")
                temp=temp.next
            print()

q=queue()

print("enter 1 to enqueue")
print("enter 2 to dequeue")
print("enter 3 to display")
print("enter 4 to exit")
while True:
    a=int(input("enter your choice: "))
    if a==1:
        n=int(input("enter the size of queue: "))
        for i in range(n):
            q.enqueue(input("enter data: "))

    elif a==2:
        q.dequeue()

    elif a==3:
        q.display()

    elif a==4:
        break
    else:
        print("invalid choice")


