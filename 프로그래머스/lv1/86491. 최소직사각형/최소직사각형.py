def solution(sizes):
    for i in sizes:
        i.sort()
    w = max(sizes)[0]
    sizes.sort(key = lambda x : x[1])
    h = sizes[-1][1]
    answer = w* h
    return answer