import sys
input = sys.stdin.readline
k, n = map(int, input().split())
li = []
for _ in range(k):
    li.append(int(input()))
li.sort()

def bs(start, end):
    if start >= end:
        return end
    cut = (start + end+1) // 2
    cnt = 0
    for i in li:
        cnt += i // cut
    if cnt >= n:
        return bs(cut, end)

    elif cnt < n:
        return bs(start, cut-1)
            
print(bs(1, max(li)))
