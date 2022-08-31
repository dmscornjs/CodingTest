import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    p = [c for c in range(1, n+1)]

    for i in range(k):
        for j in range(1, n):
            p[j] += p[j-1]
    print(p[-1])