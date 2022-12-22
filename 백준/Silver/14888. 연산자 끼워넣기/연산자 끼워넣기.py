from itertools import permutations
def xmy(x,m,y):
    if m == '+':
        return x+y
    elif m == '-':
        return x-y
    elif m == '*':
        return x*y
    elif m == '/':
        return int(x/y)

n = int(input())
a = list(map(int,input().split()))
oper = list(map(int, input().split()))
cases = ['+','-','*','/']
ml = []
for i in range(4):
    for k in range(oper[i]):
        ml.append(cases[i])

answer = []
total = list(set(permutations(ml, n-1)))
for c in total:
    sc = a[0]
    for i in range(n-1):
        sc = xmy(sc,c[i],a[i+1])
    answer.append(sc)

print(max(answer))
print(min(answer))