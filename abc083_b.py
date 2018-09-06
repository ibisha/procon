N, A, B = map(int, input().split())

total = 0
for i in range(N + 1):
    sum = 0
    tmp_i = i
    while (tmp_i > 0):
        sum += tmp_i % 10
        tmp_i = int(tmp_i / 10)
    if sum >= A and sum <= B:
        total += i
print(total)

