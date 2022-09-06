n = int(input())
li = list(map(int,input().split()))
r = li.pop(0)

for i in range(n-1):
    for j in range(1, r+1):
        if r%j == 0:
            if li[i]%j == 0:
                d = j
    print(str(r//d)+'/'+str(li[i] // d))