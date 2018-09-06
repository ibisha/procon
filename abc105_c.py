n = int(input())

s = ''

while n != 0:
    r = abs(n % 2)
    n = (n - r) // (-2)
    s = str(r) + s

if s == '':
  s = '0'

print(s)
