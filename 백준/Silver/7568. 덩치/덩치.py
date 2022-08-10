n = int(input())
li = []
for i in range(n):
    x, y = map(int, input().split())
    li.append([x,y])
h = []
for i in range(len(li)):
    c = 0
    for j in range(len(li)):
        if (li[i][0]<li[j][0]) &  (li[i][1]<li[j][1]):
            c+=1
    h.append(c+1)
print(*h)