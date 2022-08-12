n, m = map(int, input().split())

l = []
for i in range(n):
    a = input()
    l.append(a)

mn = []
for q in range(n-7):
    for e in range(m-7):
        c1 = 0
        c2 = 0
        for i in range(q, 8+q):
            for j in range(e, 8+e): 
                    if (i+j)%2 == 0:
                        if l[i][j] != 'B':
                                c1+=1
                        if l[i][j] != 'W':
                                c2+=1
                    else:
                        if l[i][j] != 'W':
                                c1+=1
                        if l[i][j] != 'B':
                                c2+=1
        mn.append(c1)
        mn.append(c2)
print(min(mn))
