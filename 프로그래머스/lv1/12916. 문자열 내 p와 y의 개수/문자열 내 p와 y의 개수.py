def solution(s):
    p = s.count('p')+ s.count('P')
    y = s.count('y')+ s.count('Y')
    if p == y:
        answer = True
    else:
        answer = False
    return answer