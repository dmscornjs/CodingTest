def solution(x, n):
    answer = []
    c = x
    for i in range(n):
        answer.append(c)
        c+=x
    return answer