import math

n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]

data_count = []
result = []
for i in range(n):
    data_count.append(data[i][0]** data[i][1])
    result.append(data_count[i]%10)

for a in result:
    print(a)
