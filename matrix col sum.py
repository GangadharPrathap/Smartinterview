n,m=map(int,input().split())
col_sum=[0]*m
for _ in range(n):
    row = list(map(int,input().split()))
    for j in range(m):
        col_sum[j]+=row[j]

for s in col_sum:
    print(s)        
