n = int(input())
a = list(map(int, input().split()))

a.sort()
a.reverse()

total = 0
for i in range(n):
    if i % 2 == 0:
        total += a[i] 
    else:
        total -= a[i]

print(total)
