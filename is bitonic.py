def is_bionic(arr):
    n=len(arr)
    i=0
    while i+1<n and arr[i]<arr[i+1]:
        i+=1
    while i+1<n and arr[i]>arr[i+1]:
        i+=1
    return i == n-1
n=int(input())
arr=list(map(int,input().split()))
print(str(is_bionic(arr)).lower())        
