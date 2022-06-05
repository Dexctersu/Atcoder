n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int, input().split()))
flag = True
for i in range(m):
    if b[i] in a:
        a.remove(b[i])
    else:
        flag = False
print("Yes") if flag else print("No")
