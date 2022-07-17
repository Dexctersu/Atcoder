n = int(input())
A = list(map(int,input().split()))
q = int(input())
m = list(map(int,input().split()))

flag = False
for bit in range(1<<n):
    total = 0
    for i in range(n):
        if bit&(1<<i):
            total+=A[i]
    if total == 21:
        flag = True

print(flag)
