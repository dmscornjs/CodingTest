n = int(input())
a = 666
c = 0

while True:
    if '666' in str(a):
        c+=1
        if c == n:
            print(a)
            break
    a+=1