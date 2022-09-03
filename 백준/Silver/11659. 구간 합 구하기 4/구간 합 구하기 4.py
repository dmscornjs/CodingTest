import sys
input = sys.stdin.readline
n, m = map(int,input().split())
nu = [0]
p = 0
li = list(map(int,input().split()))
for k in li:
    p+=k
    nu.append(p)

for i in range(m):
    a, b = map(int,input().split())
    print(nu[b] - nu[a-1])
