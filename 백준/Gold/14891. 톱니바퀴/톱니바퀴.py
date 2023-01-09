from collections import deque

t1 = deque([c for c in input()])
t2 = deque([c for c in input()])
t3 = deque([c for c in input()])
t4 = deque([c for c in input()])
k = int(input())
for i in range(k):
    tn, direct = map(int,input().split())
    if tn == 1:
        a = t1[2]
        t1.rotate(direct)
        if a != t2[6]:
            a = t2[2]
            t2.rotate(-direct)
            if a != t3[6]:
                a = t3[2]
                t3.rotate(direct)
                if a != t4[6]:
                    t4.rotate(-direct)
    
    elif tn == 2:
        a = t2[6]
        b = t2[2]
        t2.rotate(direct)
        if a != t1[2]:
            t1.rotate(-direct)
        if b != t3[6]:
            b = t3[2]
            t3.rotate(-direct)
            if b != t4[6]:
                t4.rotate(direct)

    elif tn == 3:
        a = t3[6]
        b = t3[2]
        t3.rotate(direct)
        if b != t4[6]:
            t4.rotate(-direct)
        if a != t2[2]:
            a = t2[6]
            t2.rotate(-direct)
            if a != t1[2]:
                t1.rotate(direct)

    elif tn == 4:
        a = t4[6]
        t4.rotate(direct)
        if a != t3[2]:
            a = t3[6]
            t3.rotate(-direct)
            if a != t2[2]:
                a = t2[6]
                t2.rotate(direct)
                if a != t1[2]:
                    t1.rotate(-direct)

print(int(t1[0]) + int(t2[0])*2 + int(t3[0])*4 + int(t4[0])*8)