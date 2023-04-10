import sys
input = sys.stdin.readline
n = int(input())

s = n
ans = 0

while True:
    if s < 3:
        ans = -1
        break

    elif s % 5 == 0:
        ans += s // 5
        break

    else:
        s -= 3
        ans +=1
        if s == 0:
            break

print(ans)
    