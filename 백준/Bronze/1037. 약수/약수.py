n = int(input())
li = list(map(int,input().split()))
li.sort()
if n%2 == 0:
    print(li[0]*li[-1])
else:
    print((li[(n//2)])**2)
