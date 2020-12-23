N, M, K = map(int, input().split())

n = N//2
while(n >= 0):
    if n <= M and (N - 2 * n) + (M - n) >= K:
        print(n)
        break
    else:
        n -= 1
