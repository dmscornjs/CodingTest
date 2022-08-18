a, b = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
dic = {}
for i in al:
    dic[i] = 1

for j in bl:
    try:
        dic[j] +=1
    except:
        dic[j] = 1
c=0
for k in dic:
    if dic[k] ==1:
        c+=1
print(c)