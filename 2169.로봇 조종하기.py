N, M = map(int, input().split())
L = []
for i in range(N):
    L.append(list(map(int, input().split())))

if N == 1:
    for i in range(1, M):
        L[0][i] = L[0][i]+L[0][i-1]
elif M == 1:
    for i in range(1, N):
        L[i][0] = L[i][0]+L[i-1][0]
else:
    # 첫번째 줄
    for i in range(1,M):
        L[0][i] = L[0][i]+L[0][i-1]
        
    # 두번째 줄부터 N-1줄까지
    for i in range(1,N-1):
        left = [0]*M
        right = [0]*M
        # 아래, 왼쪽
        left[0] = L[i-1][0] + L[i][0]
        for j in range(1, M):
            left[j] = max(left[j-1], L[i-1][j]) + L[i][j]
        # 아래, 오른쪽
        right[M-1] = L[i-1][M-1] +L[i][M-1]
        for j in range(M-2, -1, -1):
            right[j] = max(right[j+1], L[i-1][j]) + L[i][j]
        # 두 가지 방법 비교 최대값 저장
        for k in range(0, M):
            L[i][k] = max(left[k], right[k])
            
    # 마지막 줄
    L[N-1][0] = L[N-1][0] + L[N-2][0]
    for i in range(1, M):
        L[N-1][i] = max(L[N-1][i-1], L[N-2][i]) + L[N-1][i]

print(L[N-1][M-1])