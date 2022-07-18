S = input()
n = len(S)


ans = 0
for i in range(1 << n-1):
    for j in range(n-1):
        if i & (1 << j):
            # プラスを入れる
            pass

