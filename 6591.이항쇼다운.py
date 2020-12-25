n = [1]
k = [1]

while True:
    N, K = map(int, input().split())
    if N == 0 and K == 0:
        break
    elif N == 0 or K > N:
        break
    else:
        n.append(N)
        k.append(K)
del n[0]
del k[0]


result = []
for i in range(len(n)):
    num = n[i]
    den = min(k[i],n[i]-k[i])
    d = den
    p = 1
    if den == 0:
        result.append(1)
    elif num == den:
        result.append(1)
    else:
        for j in range(den-1,0,-1):
            num = num * (n[i]-p)
            d = d * (den-p)
            p += 1
        result.append(num//d)

for r in result:
    print(r)
