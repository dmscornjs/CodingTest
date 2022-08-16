x = input()
result = 0
idx = x.find('-')

if idx >=0:
    minus = x[idx:]
    minus = minus.replace('-','+')
    
    x = x[:idx]
    b = minus.split('+')
    for j in b:
        if j != '':
            result-=int(j)
            
a = x.split('+')    
for i in a:
    if i != '':
        result+=int(i)              

print(result)
