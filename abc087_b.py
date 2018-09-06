coin500 = int(input())
coin100 = int(input())
coin50 = int(input())
total = int(input())

ans = 0
for i_500 in range(coin500 + 1):
    for i_100 in range(coin100 + 1):
        for i_50 in range(coin50 + 1):
            if 500 * i_500 + 100 * i_100 + 50 * i_50 == total:
                ans += 1
print(ans)
