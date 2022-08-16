import sys
input = sys.stdin.readline
n, m = map(int,input().split())
s = {}
for i in range(n):
    a = input()
    s[a] = 1
c = 0
for j in range(m):
    b = input()
    try:
        c += s[b]
    except:
        continue
print(c)
    