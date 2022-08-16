import sys
input = sys.stdin.readline
n, m = map(int,input().split())
dic = {}
for i in range(n):
    a = input().rstrip()
    dic[a] = i+1
    dic[str(i+1)] = a
    
for j in range(m):
    b = input().rstrip()
    print(dic[b])
