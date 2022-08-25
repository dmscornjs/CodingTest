cham = int(input())
lia = []
lib = []
s = []
for i in range(6):
    a, b = map(int,input().split())
    if a not in s:
        s.append(a)
    else:
        s.remove(a)
    #li.append(list([a,b]))
    lia.append(a)
    lib.append(b)
print(cham*((lib[lia.index(s[0])] * lib[lia.index(s[1])])-(lib[lia.index(s[0])-3] * lib[lia.index(s[1])-3])))
