n=int(input("enter the number:"))
su=0
if(n<0):
    n=n*-1
while(n!=0):
    rem=n%10
    su=su+rem
    n=n//10
print("sum of digits=",su)