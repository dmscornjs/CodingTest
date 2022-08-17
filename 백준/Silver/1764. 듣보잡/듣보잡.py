n, m = map(int,input().split())
dic = {}
ans = []
c=0
for i in range(n):
    a = input()
    dic[a] = 1
for j in range(m):
    b = input()
    if b in dic:
        ans.append(b)
        
ans.sort()
print(len(ans))
for k in ans:
    print(k)
