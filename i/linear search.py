def linearSearch(arr,n):
    for i in range(n):
        if arr[i]==n:
            return "key found at index",i
    return " key not found"

arr=list(map(int,input("enter elements").split()))
n=int(input("enter key to find"))
print(linearSearch(arr,n))