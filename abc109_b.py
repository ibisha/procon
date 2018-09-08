n = int(input())
w = [input() for _ in range(n)]

correct = True
for i in range(len(w)):
    if w[i] in w[i + 1:]:
        correct = False
        break
    if i > 0 and w[i][0] != w[i - 1][-1]:
        correct = False
        break

if correct:
    print("Yes")
else:
    print("No")
