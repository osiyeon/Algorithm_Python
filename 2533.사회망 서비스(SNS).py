def newP():
    for x in earlyAdaptor:
        for i in range(N+1):
            if x in P[i]:
                P[i].remove(x)
N = int(input())

P = list([] for _ in range(N+1))

for i in range(N-1):
    u, v = map(int, input().split())
    P[u].append(v)
    P[v].append(u)

# print(P)

earlyAdaptor = []
a = 1
while(len(P[a])!=0):
    for i in range(N+1):
        if len(P[i])==1:
            a = P[i].pop()
            print("index: ", a)
            if len(P[a])!=0:
                earlyAdaptor.append(a)
    earlyAdaptor = list(set(earlyAdaptor))
    newP()
    print("P:", P)
print(len(earlyAdaptor))