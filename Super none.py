n,m=map(int,input().split())
mat=[list(map(int,input().split())) for _ in range(n)]
found = False

for i in range(1,n-1):
    for j in range(1,m-1):
        if mat[i][j] == 1:
            ok=True
            for di in (-1,0,1):
                for dj in (-1,0,1):
                    if di==0 and dj==0:
                        continue
                    if mat[i+di][j+dj]!=0:
                        ok = False
            if ok:
                found = True
                break
    if found:
        break
print("Yes" if found else "No")        
Su
