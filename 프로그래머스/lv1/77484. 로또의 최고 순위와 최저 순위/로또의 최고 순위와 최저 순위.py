def solution(lottos, win_nums):
    lottos.sort()
    win_nums.sort()
    zero = lottos.count(0)
    c = 0
    l = lottos.copy()
    wn = win_nums.copy()
    for i in lottos:
        if i in win_nums:
            l.remove(i)
            wn.remove(i)
            c +=1
    a = 7 - (zero+c)
    b = 7 - c
    if a > 6:
        a = 6
    if b > 6:
        b = 6
    answer = [a, b]
    return answer