n, k = map(int, input().split())

p = n // k
ans = 0

if k % 2:
    print(p ** 3)
else:
    for i in range(1, n + 1):
        if i % k == k //2:
            ans += 1
    print(p ** 3 + ans ** 3)
