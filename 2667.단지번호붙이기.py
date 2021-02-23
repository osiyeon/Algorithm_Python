count = 1

def checkAround( num, n, m):
    global count
    count += 1
    if m+1 < N and G[n][m+1] == '1': # 위
        G[n][m+1] = num
        checkAround( num, n, m+1)
    if n+1 < N and G[n+1][m] == '1' : # 아래
        G[n+1][m] = num
        checkAround( num, n+1, m)
    if m-1 >=0 and G[n][m-1] == '1' : # 왼쪽
        G[n][m-1] = num
        checkAround(num, n, m-1)
    if n-1 >= 0 and G[n-1][m] == '1' : # 위
        G[n-1][m] = num
        checkAround(num, n-1, m)
    return count
    
N = int(input())

G = []
for i in range(N):
    G.append(list(input()))

num = 2
counts = []
for j in range(N):
    for i in range(N):
        if G[j][i] == '1':
            count = 1
            G[j][i] = num
            result = checkAround( num, j, i)
            counts.append(result)
            num += 1
        
counts = sorted(counts)
print(num-2)
for c in counts:
    print(c-1)


