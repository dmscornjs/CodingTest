def solution(n):
    i = 1
    while True: 
        if (3 ** i) > n:
            t = i-1
            break
        i+=1
    print(i)
    n3 = ''

    for j in range(i):
        n3 += str(n // (3**t))
        n = n%3**t
        t -=1
    rn3 = n3[::-1]
    p = i -1
    answer = 0
    for k in range(i):
        answer += int(rn3[k]) * 3**p
        p -=1
    return answer