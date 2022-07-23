S = list(input())
n = len(S)


ans = 0
for bit in range(1 << n-1):
    # 式
    formula = S[0]
    for i in range(n-1):
        if (bit & (1 << i)):
            formula += "+"+S[i+1]
        else:
            formula += S[i+1]
    ans += eval(formula)
print(ans)
