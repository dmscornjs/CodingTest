n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
l = []
for i in a:
    if i >= b:
        l.append(i-b)
    else:
        l.append(0)
ans = n
for u in l:
    ans += ((u -1)//c) +1
print(ans)