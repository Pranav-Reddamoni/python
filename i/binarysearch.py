def binarySearch(arr,key,low,high):
    while(low<=high):
        mid=(low+high)//2

        if arr[mid]==key:
            return "key found at index",mid
        elif key<arr[mid]:
            high=mid-1
        elif key>arr[mid]:
            low=mid+1
    return "key not found"

arr=list(map(int,input("enter elements").split()))
key=int(input("enter key to find"))
print(binarySearch(arr,key,0,len(arr)-1))