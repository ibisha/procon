N = int(input())

total = 0
for num in range(1, N + 1):
    if num % 2 == 0:
        continue
    divisors = 0
    for i in range(1, num + 1):
        if num % (i + 1) == 0:
            num = num / (i + 1)
            divisors += 1
    if divisors == 3:
        total += 1

print(total)

