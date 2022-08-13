n, k = map(int,input().split())
ai = []
for i in range(n):
    a = int(input())
    ai.append(a)

count = 0
change = k

for j in range(len(ai)):
    i = ai.pop(-1)
    x = change//i
    count += x
    change -= i*x

print(count)