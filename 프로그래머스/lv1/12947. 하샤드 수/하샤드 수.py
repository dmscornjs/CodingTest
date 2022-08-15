def solution(x):
    s = sum(int(c) for c in str(x))
    if x % s == 0:
        answer = True
    else:
        answer = False
    return answer