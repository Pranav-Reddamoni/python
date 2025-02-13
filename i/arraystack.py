def push(data):
    if len(l)<n:
        l.append(data)
    else:
        print("stack is overflow")

def pop():
    if l:
        l.pop()
    else:
        print('stack is underflow')

def display():
    print(l)
l=[]
print("enter 1 to push")
print("enter 2 to pop")
print("enter 3 to display")
print("enter 4 to quit")
while True:
    a=int(input("\nenter the option"))
    if a==1:
        n=int(input("\nEnter size of stack: "))
        for i in range(n):
            push(input("Enter data: "))

    elif a==2:
        pop()

    elif a==3:
        display()

    elif a==4:
        break
    else:
        print("enter crct option")



