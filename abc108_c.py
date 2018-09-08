n, k = map(int, input().split())

nums = [0] * k
for i in range(1, n + 1):
    nums[i % k] += 1

ans = 0
for a in range(k):
    b = (k - a) % k
    c = (k - a) % k
    if (b + c) % k == 0:
        ans += nums[a] * nums[b] * nums[c]
print(ans)

