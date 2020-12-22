A, B, C = map(int, input().split())

if B >= C:
    print(-1)
else:
    sales_rate = A//(C-B)+1
    print(sales_rate)


print(3//2)
print(3/2)