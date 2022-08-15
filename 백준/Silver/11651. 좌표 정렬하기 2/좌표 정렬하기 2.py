import sys
input = sys.stdin.readline
n = int(input())
li = []
for i in range(n):
    x, y = map(int, input().split())
    li.append([x,y])
    
li.sort()
li.sort(key = lambda x : x[1])

for o in li:
    print(o[0],o[1])
