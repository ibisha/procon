n, m, qq = map(int, input().split())
lr = [[0] * n for _ in range(n)]
for _ in range(m):
    l, r = map(int, input().split())
    lr[l - 1][r - 1] += 1

for i in range(n):
    for j in range(n - 1):
        lr[i][j + 1] += lr[i][j]
for j in range(n):
    for i in range(n-1, 0, -1):
        lr[i - 1][j] += lr[i][j]

for _ in range(qq):
    p, q = map(int, input().split())
    if q == n:
        print(lr[p - 1][q - 1])
    else:
        print(lr[p - 1][q - 1] - lr[q][q - 1])
