n = int(input())
dic = [0] * 1000001

for i in range(2, n+1):
    dic[i] = dic[i-1] +1
    if i % 2 == 0:
        dic[i] = min(dic[i], dic[i // 2] +1) 
    if i % 3 == 0:
        dic[i] = min(dic[i], dic[i // 3] +1)

print(dic[n])
    
