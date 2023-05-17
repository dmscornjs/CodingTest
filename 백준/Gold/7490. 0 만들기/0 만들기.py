from itertools import product
import sys
input = sys.stdin.readline
t = int(input())
li = [' ','+','-']
for a in range(t):
    n = int(input())
    num = [c for c in range(1,n+1)]
    data = product(li, repeat=n-1)
    ans = []
    for d in data:
        s = '1'
        for i in range(n-1):
            s += str(d[i]) + str((i+2))
        sd = s.replace(" ","")
        if (eval(sd))==0:
            print(s)
    if a != t-1:
        print()