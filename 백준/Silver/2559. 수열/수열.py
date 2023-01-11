n, k = map(int, input().split())
li = list(map(int, input().split()))
if k == 1:
    print(max(li))
elif k == n:
    print(sum(li))
else:
    nu = [0]
    num = 0
    for i in li:
        num+=i
        nu.append(num)
    ans = []
    for j in range(n-k+1):
        ans.append(nu[j+k] - nu[j]) 
    print(max(ans))
 