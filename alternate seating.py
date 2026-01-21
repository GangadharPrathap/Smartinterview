n=int(input())
m=int(input())
seats = list(map(int,input().split()))
c=0
for i in range(m):
    if seats[i]==0:
        left_ok = (i==0) or (seats[i-1]==0)
        right_ok = (i==m-1) or (seats[i+1]==0)
        if left_ok and right_ok:
            seats[i] =1
            c +=1
if c >= n:
    print("YES")
else:
    print("NO")                
