x = int(input())
d = list(map(int,input().split()))
l = list(map(int,input().split()))


for i in range(x-1):
    if l[i] < l[i+1]:
        l[i+1]=l[i]

l.pop(-1)

pay = 0
for j in range(x-1):
    pay += d[j] * l[j]

print(pay)