given = ["dreamer", "dream", "eraser", "erase"]
S = input()

while len(s) > 0:
    judge = [s.endswith(i) for i in given]
    if any(judge):
        target = given[judge.index(True)]
        s = s[:-len(target)]
        if len(s) == 0:
            print("YES")
            break
    else:
        print("NO")
        break


