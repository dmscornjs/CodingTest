n = int(input())
m = int(input())
s = input()

p = 'IO' * n + 'I'
ans = 0
for i in range(m-(2*n+1)):
    if s[i] == 'I':
        if s[i:i+(2*n+1)] == p:
            ans +=1
print(ans)