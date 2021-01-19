N = int(input())

DP = [0]*(N+1)
B = [0]*((N-4)//2+1)
for n in range(1, N+1):
    if n == 2:
        DP[n] = 3
    elif n==4:
        DP[n] = DP[2]*DP[2] + 2
    else:
        if n % 2 == 0:
            i = (n-4)//2
            B[i] = 2*DP[i*2] + B[i-1]
            DP[n] = DP[2]*DP[n-2] + B[i] + 2

print(DP[N])
    
