n = int(input())
nums = list(map(int, input().split()))
cnt = 0
while all(num % 2 == 0 for num in nums):
    nums = [num / 2 for num in nums]
    cnt += 1
print(cnt)
