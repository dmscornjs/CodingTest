def com(m, n):
    a = 1
    for u in range(m, m-n, -1):
        a *= u
    for j in range(2,n+1):
        a //= j
    return int(a)


t = int(input())
for i in range(t):
    n , m = map(int, input().split())
    print(com(m, n))