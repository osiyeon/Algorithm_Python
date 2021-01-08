N = int(input())

DP = [0] * (N+1)
for n in range(2, N+1):
    if n <= 3:
        DP[n] = 1
    elif n % 2 == 0 and n % 3 == 0:
        DP[n] = min(DP[n//3], DP[n//2]) + 1
    elif n % 2 == 0:
        DP[n] = min(DP[n//2], DP[n-1]) + 1
    elif n % 3 == 0:
        DP[n] = min(DP[n//3], DP[n-1]) + 1
    else:
        DP[n] = DP[n-1] + 1

print(DP[N])