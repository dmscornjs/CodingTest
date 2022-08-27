import sys
def uc(a,b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    if a % b == 0:
        return b
    else:
        return uc(b, a%b)

input = sys.stdin.readline    
t = int(input())
for i in range(t):
    a, b = map(int,input().split())
    print(a*b//uc(a,b))
