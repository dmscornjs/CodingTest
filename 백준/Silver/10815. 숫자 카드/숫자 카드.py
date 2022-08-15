import sys
n = int(input())
x = list(map(int,input().split()))
m = int(input())
y = list(map(int,input().split()))

a = [0] * 20000001

for i in x:
    a[i-10000000] = 1

for j in y:
    print(a[j-10000000])