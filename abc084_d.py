maxnum = 100000

# エラトステネスのふるい
is_prime = [x for x in range(maxnum)]
for prime in is_prime:
    if prime == 0 or prime == 1:
        is_prime[prime] = 0
        continue
    for non_prime in range(prime * 2, maxnum, prime):
        is_prime[non_prime] = 0

like_sum = [0] * maxnum
for i in range(3, maxnum):
    like_sum[i] = like_sum[i - 1]
    if (is_prime[i] and is_prime[(i + 1) // 2]):
        like_sum[i] += 1

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(like_sum[r] - like_sum[l - 1])
