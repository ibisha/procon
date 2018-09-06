import sys
n, k = map(int, input().split())

for x in range(min(n, int(k / 10000)) + 1):
    for y in range(min((n - x), int((k - 10000 * x)/ 5000)) + 1):
        z = n - x - y
        if 10000 * x + 5000 * y + 1000 * z == k:
            print("{} {} {}".format(x,y,z))
            sys.exit()

print("{} {} {}".format(-1,-1,-1))
