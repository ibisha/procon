n = int(input())
c = [0] * n
s = [0] * n
f = [0] * n
for i in range(n - 1):
    c[i], s[i], f[i] = map(int, input().split())

for i in range(n - 1):
    total = 0
    for j in range(i, n - 1):
        if total < s[j]:
            total = s[j]
        elif ((total - s[j]) % f[j]) != 0:
            total += f[j] - total % f[j]
        total += c[j]
    print(total)
print(0)
