s = list(input())
k = int(input())

ans = 1
for i in range(k):
    num = s[i]
    if num != "1":
        ans = num
        break
print(ans)
