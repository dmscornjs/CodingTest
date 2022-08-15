x = [0]*20000001
n = int(input())
a = list(map(int, input().split()))
for i in a:
    x[i+10000000] +=1
m = int(input())
b = list(map(int, input().split()))
for j in b:
    print(x[j+10000000])
