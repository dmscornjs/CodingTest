n, m = map(int,input().split())
li = list(map(int,input().split()))
start = 0
end = max(li)

while (start<=end):
    t = (start + end) //2
    c = 0
    for i in li:
        if i > t:
            c += i - t
    if c<m:
        end = t-1
    else:
        ans = t
        start = t+1

print(ans)
    
