n, k = map(int,input().split())
ans = 1

for i in range(1, k+1):
    ans = ans * (n-i+1)

for j in range(2, k+1):
    ans = ans//j

print(int(ans%10007))
