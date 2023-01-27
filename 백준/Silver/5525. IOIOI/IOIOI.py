n = int(input())
m = int(input())
s = input()

p = 'IO' * n + 'I'
ans = 0
for i in range(m-len(p)):
    if s[i:i+len(p)] == p:
        ans +=1
print(ans)