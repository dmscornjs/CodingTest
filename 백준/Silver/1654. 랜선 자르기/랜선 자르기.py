k, n = map(int, input().split())
li = []
for i in range(k):
    li.append(int(input()))
start = 0
end = max(li)
while (start <= end):
    t = (start + end+1)//2
    c = 0
    for i in li:
        c += i//t

    if c<n:
        end = t-1

    else:
        ans = t
        start = t+1

print(ans)
    