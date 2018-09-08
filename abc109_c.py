from functools import reduce

n, start = map(int, input().split())
x = list(map(int, input().split()))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

sa = [0] * n
for i in range(n):
    sa[i] = abs(start - x[i])

print(reduce(gcd, sa))
