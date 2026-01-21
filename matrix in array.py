n,m = map(int,input().split())
mat=[]
for _ in range(n):
    mat.append(list(map(int,input().split())))

a=int(input())
arr=set(map(int,input().split()))

for row in mat:
    count=0
    for x in row:
        if x in arr:
            count+=1
    print(count)        
