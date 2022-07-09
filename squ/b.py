n = int(input())
A = []
B = []
for i in range(n):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)

ans = []

for i in range(100):
    for j in range(i,101):
        dis = 0
        for k in range(n):
            dis += abs(A[k]-i)+abs(A[k]-B[k])+abs(B[k]-j)
        ans.append(dis)
print(min(ans))
