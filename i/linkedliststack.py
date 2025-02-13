class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class stack:

    top = 0

    def __init__(self):
        self.head = None

    def push(self,data):
        newnode = node(data)
        if self.top<self.capacity :
            print(newnode.data,"is pushed")
            newnode.next = self.head
            self.head = newnode
            self.top+=1
        else:
            print("stack overflow")

    def pop(self):
        if self.top>0:
            print(self.head.data,"is popped")
            self.head = self.head.next
            self.top-=1
        else:
            print("stack underflow")

    def peek(self):
        if self.top>0:
            print(self.head.data,"is at the top of the stack")
        else:
            print("stack underflow")

    def display(self):
        if self.top <= 0:
            print("Stack is Empty")
        else:
            print("Stack:- ", end='')
            temp = self.head
            while temp:
                print(temp.data, end='<-')
                temp = temp.next
            print()
s=stack()
print("enter 1 to push")
print("enter 2 to pop")
print("enter 3 to display")
print("enter 4 to quit")
while True:
    a=int(input("\nenter the option"))
    if a==1:
        s.capacity=int(input("\nEnter size of stack: "))
        for i in range(s.capacity):
            s.push(input("Enter data: "))

    elif a==2:
        s.pop()

    elif a==3:
        s.display()

    elif a==4:
        break

    else:
        print("enter crct option")

