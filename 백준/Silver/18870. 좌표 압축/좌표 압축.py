n = int(input())
x = list(map(int, input().split()))
u = list(set(x))
u.sort()
dic = {}
c = 0
for i in u:
    dic[i] = c
    c+=1
for k in x:
    print(dic[k], end = ' ')