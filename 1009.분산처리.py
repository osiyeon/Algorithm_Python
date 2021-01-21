n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]

result = []
for i in range(n):
    if data[i][0] % 10 == 0:
        result.append(10)
    else:
        result.append(pow(data[i][0],data[i][1], 10))

for a in result:
    print(a)
