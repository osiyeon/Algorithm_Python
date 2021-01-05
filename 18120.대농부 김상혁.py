# 47.57 + 38.19660 + 15.278640 + 12.010
import math
import decimal

N, A = map(int, input().split())

n = [list(map(int, input().split())) for _ in range(N)]

cost = 0
profit = 0

r = 0
while(True):
    cost  = A * r * r
    newprofit = 0
    netprofit = 0
    print("r: ", r)
    for i in range(len(n)):
        if r >= math.sqrt(n[i][0]**2 + n[i][1]**2):
            newprofit += (r - math.sqrt(n[i][0]**2 + n[i][1]**2)) * n[i][2]
            print("np: ", newprofit)
    # newprofit = round(newprofit, 6)
    print("newprofit:",newprofit)
    print("cost:", cost)
    netprofit = newprofit - cost #순이익
    print("netprofit: ", netprofit)
    print("--------")
    if netprofit > profit:
        profit = netprofit
        r += 1
    elif netprofit <= 0:
        r += 1
    else:
        break

if r == 0:
    result = 0
else:
    result = profit
print(result)