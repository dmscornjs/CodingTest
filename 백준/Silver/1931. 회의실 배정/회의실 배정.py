import sys
n = int(sys.stdin.readline())
x = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    x.append([a,b])

x.sort(key=lambda x:x[0])
x.sort(key=lambda x:x[1])
#x[:][1].sort()

cnt = 1
end = x[0][1]

for i in x[1:]:
    if i[0] >= end:
        end = i[1]
        cnt +=1
print(cnt)