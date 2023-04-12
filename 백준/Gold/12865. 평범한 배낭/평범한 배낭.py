import sys
input = sys.stdin.readline
n , k = map(int, input().split())
w = [0] * (n+1) 
v = [0] * (n+1) 
dp = [[0]* (k+1) for _ in range(n+1)]

for i in range(1,n+1):
    w[i], v[i] = map(int, input().split())

for i in range(1, n+1):
    for j in range(1, k+1):
        if j >=w[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][k])