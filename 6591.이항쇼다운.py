n = [0]
k = [0]

n[0], k[0] = map(int, input().split())

while n[-1] != 0 and k[-1] != 0:
    N, K = map(int, input().split())
    n.append(int(N))
    k.append(int(K))

result = []
i = 0
while i != len(n)-1:
    num = n[i]
    den = k[i]
    p = 1
    for j in range(k[i],1,-1):
        num = num * (n[i]-p)
        den = den * (k[i]-p)
        p += 1
    result.append(num//den)
    i += 1


print(result)
