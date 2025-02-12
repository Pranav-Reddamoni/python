n=int(input("enter the key range"))
d={}
for i in range(n):
    print("key=",i+1)
    k=i+1
    v=input("enter the value")
    d[k]=v
print(d)
print()
print(d.keys())
print()
print(d.values())
print()
print(d.items())