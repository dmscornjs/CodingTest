def fib(n):
    global c1
    if n == 1 or n == 2:
        c1+=1
        return 1
    return fib(n-1) + fib(n-2)

def fibo(n):
    global c2
    if f[n] != 0:
        return f[n]
    c2+=1
    f[n] = fibo(n-1) + fibo(n-2)
    return f[n]
    
n = int(input())    
f = [0] *41
f[1] = 1
f[2] = 1
c1 = 0
c2 = 0
fib(n)
fibo(n)
print(c1, c2)