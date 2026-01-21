n=int(input())
arr = list(map(int,input().split()))
total = sum(arr)
if total%3!=0:
    print("false")
else:
    target =total//3
    curr=0
    parts=0

    for i in range(n):
        curr+= arr[i]
        if curr ==target:
            parts+=1
            curr=0
    if parts>=3:
        print("true")
    else:
        print("false")                
