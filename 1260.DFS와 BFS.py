def DFS(v): # v를 방문중
    visited_DFS[v] = True
    path_DFS.append(v)
    for w in range(1,N+1):
        if visited_DFS[w] == False and G[v][w] == 1:
            DFS(w)
    # v에 인접한 모든 노드 고려함
    # backtrack

def BFS(v): # v를 방문중
    visited_BFS[v] = True
    Q = []
    Q.insert(0, v)
    while len(Q) > 0:
        v = Q.pop()
        if v not in path_BFS:
            path_BFS.append(v)
        for w in range(1, N+1):
            if visited_BFS[w] == False and G[v][w] == 1:
                visited_BFS[v] = True
                Q.insert(0, w)

N, M, V = map(int, input().split())

G = []
for i in range(N+1):
    G.append([0]*(N+1))

for i in range(M):
    v, w = map(int, input().split())
    G[v][w] = 1 
    G[w][v] = 1

visited_DFS = [False]*(N+1)
path_DFS = []
DFS(V)

visited_BFS = [False]*(N+1)
path_BFS = []
BFS(V)

for x in range(len(path_DFS)-1):
    print(path_DFS[x], end=' ')
print(path_DFS[-1])
for x in range(len(path_BFS)-1):
    print(path_BFS[x], end=' ')
print(path_BFS[-1])

