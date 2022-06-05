n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int, input().split()))
eacted = [False for _ in range(n)]
for i in range(m):
    # 食べれるものがあるかを判定
    flag = False
    for j in range(n):
        if(a[j] == b[i] and not(eacted[j])):
            eacted[j] = True
            flag = True
            break
    if(not(flag)):
        print("No")
        exit()
print("Yes")

# flag = True
# for i in range(m):
#     if b[i] in a:
#         a.remove(b[i])
#     else:
#         flag = False
# print("Yes") if flag else print("No")
