n = int(input())
ans = []
def m(a):
    if a == 1:
        for i in ans:
            print(i)
    for i in range(2, a+1):
        if a % i == 0:
            ans.append(i)
            return(m(a//i))

m(n)