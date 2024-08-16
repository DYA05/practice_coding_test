N = input()
NN = list(map(int, input().split()))
M = input()
MM = list(map(int, input().split()))

ans = ['0'] * len(MM)

mn = list(set(NN) & set(MM))

for i in mn:
    ans[MM.index(i)] = '1'

print(' '.join(ans))


# dictionary로 해야 시간초과 안남
# 그냥 set으로 하는것도 방법



