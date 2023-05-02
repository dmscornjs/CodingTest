import sys
from collections import deque
input = sys.stdin.readline
t1 = deque([c for c in input().rstrip()])
t2 = deque([c for c in input().rstrip()])
t3 = deque([c for c in input().rstrip()])
t4 = deque([c for c in input().rstrip()])

k = int(input())
for _ in range(k):
    tn, d = map(int, input().split())

    if tn == 1:
        if t1[2] != t2[6]:
            t1.rotate(d)
            if t2[2] != t3[6]:
                t2.rotate(-d)
                if t3[2] != t4[6]:
                    t3.rotate(d)
                    t4.rotate(-d)
                else:
                    t3.rotate(d)
            else:
                t2.rotate(-d)
        else:
            t1.rotate(d)
    elif tn == 2:
        if t2[2] != t3[6]:
            if t3[2] != t4[6]:
                t4.rotate(d)
            t3.rotate(-d)
        if t2[6] != t1[2]:
            t1.rotate(-d) 
        t2.rotate(d)
    
    elif tn == 3:
        if t3[6] != t2[2]:
            if t2[6] != t1[2]:
                t1.rotate(d)
            t2.rotate(-d)
        if t3[2] != t4[6]:
            t4.rotate(-d) 
        t3.rotate(d)

    elif tn == 4:
        if t4[6] != t3[2]:
            t4.rotate(d)
            if t3[6] != t2[2]:
                t3.rotate(-d)
                if t2[6] != t1[2]:
                    t2.rotate(d)
                    t1.rotate(-d)
                else:
                    t2.rotate(d)
            else:
                t3.rotate(-d)
        else:
            t4.rotate(d)

print(int(t1[0]) + (int(t2[0])*2) + (int(t3[0]) *4)+ (int(t4[0])*8))