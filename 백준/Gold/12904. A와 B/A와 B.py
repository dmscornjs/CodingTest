s = input()
t = input()

for i in range(len(t)-len(s)):
    #print(t)
    if t[-1] == 'A':
        t = t[:-1]
    else:
        t = t[:-1]
        t = t[::-1]

if t == s:
    print(1)
else:
    print(0)
