import math

def solution(n):
    check = [True for c in range(2, n+1)]
    for i in range(2, int(math.sqrt(n)+1)):
        for j in range(i+i, n+1, i):
            check[j-2] = False
    return sum(check) 