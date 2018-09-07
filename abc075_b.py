h,w = map(int, input().split())
s = [list(input()) for i in range(h)]

ans = [[0 for _ in range(w + 2)] for _ in range(h + 2)]

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            ans[i][j] += 1
            ans[i][j + 1] += 1
            ans[i][j + 2] += 1
            ans[i + 1][j] += 1
            ans[i + 1][j + 1] = '#'
            ans[i + 1][j + 2] += 1
            ans[i + 2][j] += 1
            ans[i + 2][j + 1] += 1
            ans[i + 2][j + 2] += 1

for i in range(1, h + 1):
    for j in range(1, w + 1):
        print(ans[i][j], end="")
    print()
