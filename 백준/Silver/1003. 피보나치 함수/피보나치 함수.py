import sys
input = sys.stdin.readline

def fib(n):
    if n == 0:
        global z
        z +=1
        return [1, 0]
    elif n == 1:
        global one
        one +=1
        return [0, 1]
    elif d[n] != -1:
        return d[n]
    else:
        d[n] = [fib(n-1)[0] + fib(n-2)[0],fib(n-1)[1] + fib(n-2)[1]]
        return d[n]

t = int(input())
d = [-1] * 50
for i in range(t):
    n = int(input())
    z = 0
    one = 0
    print(*fib(n))