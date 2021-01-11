def numOfPaths(n):
    if DP[n] == 0:
        if n <= M-1:
            DP[n] = 1
        elif n % M == 0:
            DP[n] = 1
        else:
            DP[n] = DP[n-1] + DP[n-M]
    return DP[n]


N, M, O = map(int, input().split())
DP = [0]*(N*M)

firstResult = 1
if O != 0:
    for i in range(1, O):
        firstResult = numOfPaths(i)
if O == 0:
    O = 1
for i in range(O, N*M):
    result = numOfPaths(i-(O-1))

print(firstResult * result)


