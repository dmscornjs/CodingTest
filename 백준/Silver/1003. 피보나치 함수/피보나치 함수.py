import sys
input = sys.stdin.readline

t = int(input())

dp = [[0] for _ in range(42)]
dp[0] = (1, 0)
dp[1] = (0, 1)
#dp = [(1, 0), (0, 1)]

for i in range(2, 42):
    dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])

for _ in range(t):
    x = int(input())
    print(dp[x][0], dp[x][1])