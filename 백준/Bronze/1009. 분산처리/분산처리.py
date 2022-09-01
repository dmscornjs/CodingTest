import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    a, b = map(int,input().split())
    c = a % 10
    for i in range(1, b):
        c = c * a %10
    if c%10 == 0:
        print(10)
    else:
        print(c%10)