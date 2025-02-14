import queue


def enqueue(data):
    global front
    global rear

    if front==-1 and rear==-1:
        queue.append(data)
        front=0
        rear=0
        print(queue[rear],"is enqueued")
    else:
        rear=rear+1
        queue.append(data)
        print(queue[rear],"is enqueued")

def dequeue():
    global front
    global rear
    if front==-1 and rear==-1:
        print("Queue is empty")
    elif front==0 and rear==0:
        print(queue[front],"is dequeued")
        queue.pop(0)
        front=rear=-1
    else:
        print(queue[front],"is dequeued")
        queue.pop(0)
        rear-=1

def display():
    if queue:
        print(queue)
    else:
        print("Queue is empty")

queue=[]
front=-1
rear=-1
print("enter 1 to enqueue")
print("enter 2 to dequeue")
print("enter 3 to display")
print("enter 4 to exit")
while True:
    a=int(input("enter your choice: "))
    if a==1:

        n=int(input("enter the size of queue: "))
        for i in range(n):
            enqueue((input("enter the data: ")))

    elif a==2:
        dequeue()
    elif a==3:
        display()
    elif a==4:
        break
    else:
        print("invalid choice")
