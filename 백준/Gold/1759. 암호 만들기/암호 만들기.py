import sys
from itertools import combinations
input = sys.stdin.readline
l, c = map(int, input().split())
s = list(map(str, input().split()))
m = ['a','e','i','o','u']
s.sort()
#ans = []
for i in combinations(s, l):
    t = 0
    for a in m:
        if a in i:
            t +=1
    if t>=1:
        if (l-t)>=2:
            st = ''.join(list(i))
            print(st)