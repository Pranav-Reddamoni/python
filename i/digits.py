n=int(input("enter digits:"))
if(n<0):
    n=n*-1
i=0
while(n>0):
    n=n//10
    i+=1
print(i)