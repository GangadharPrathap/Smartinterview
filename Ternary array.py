n=int(input())
arr=list(map(int,input().split()))
cost=0
for x in arr:
    best=float('inf')
    for b in (0,1,2):
        if b!=x:
            best = min(best,abs(x-b))
    cost+=best
print(cost)    
