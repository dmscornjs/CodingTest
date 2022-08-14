n = input()
li = []
for i in n:
    li.append(i)
li.sort(reverse = True)
ans = ''
for j in li:
    ans +=j
    
print(ans)
