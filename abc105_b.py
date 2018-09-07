n = int(input())
 
isExist = False

for i in range(int(n / 7) + 1):
  for j in range(int(n / 4) + 1):
    if (7 * i + 4 * j == n):
      isExist = True
      break

if isExist:
  print("Yes")
else:
  print("No")
