n=int(input())
i,j,k,l=map(int,input().split())
total =0
for r in range(n):
    row = list(map(int,input().split()))
    if i<= r<= k:
        for c in range(j,l+1):
            total += row[c]
print(total)            
