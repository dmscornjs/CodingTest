li = []
for i in range(3):
    li.append(list(map(int,input().split())))
x = []
y = []
for k in li:
    if k[0] in x:
        x.remove(k[0])
    else:
        x.append(k[0])
for k in li:        
    if k[1] in y:
        y.remove(k[1])
    else:
        y.append(k[1])

print(x[0],y[0])
