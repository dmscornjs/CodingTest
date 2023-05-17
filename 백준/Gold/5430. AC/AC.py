import sys
#from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = input()
    n = int(input())
    if n == 0:
        input()
        li=[]
    else:
        ar = input()[1:-2]
        li = list(map(int, ar.split(',')))

    if p.count('D') > n:
        print('error')
    else:
        direct = 1
        for i in p:
            if i == 'R':
                direct *= -1
                #li.reverse()
            elif i == 'D':
                if direct == 1:
                    li.pop(0)
                elif direct == -1:
                    li.pop()
                else:
                    li = 'error'
                    break
        if direct == -1:
            li.reverse()
        ans = str(li).replace(" ","")
        print(ans)
    