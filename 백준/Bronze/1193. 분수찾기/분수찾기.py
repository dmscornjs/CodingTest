n = int(input())
a=1
b=1
c = 0
j = 0
az = 0
bz = 0
while True:
    c+=j
    if c >=n:
        s = j*(j-1)//2
        if (j-1)%2 == 0:
            a = j-1
        else:
            b = j-1
        #print(a, b)
        #print(s)
        break
    j+=1
for i in range(s, n):
    #print(a, b, i)
    if (a == 1) & (az ==0):
        b +=1
        az = 1
        bz = 0
    elif (b == 1) & (bz == 0):
        a +=1
        bz = 1
        az = 0
    elif az == 1:
        a +=1
        b -=1
    else:  #bz == 1
        a -=1
        b+=1
print(str(a)+"/"+str(b))