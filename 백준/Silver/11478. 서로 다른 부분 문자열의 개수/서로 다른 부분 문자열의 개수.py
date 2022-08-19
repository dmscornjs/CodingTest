s=input()
dic = {}

for i in range(len(s)):
    for j in range(len(s)-i):
        a = s[j:j+i+1]
        if a in dic:
            dic[a] +=1
        else:
            dic[a] = 1


print(len(dic))
