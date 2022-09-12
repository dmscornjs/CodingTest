n = int(input())
c = 0
x = n
while True:
    if x <0:
        print(-1)
        break
    elif x % 5 == 0:
        c+=(x//5)
        print(c)
        break
    x -=3
    c+=1
