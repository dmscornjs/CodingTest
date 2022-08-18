def solution(s):
    answer = False
    if (len(s) == 4) or (len(s) == 6):
        try:
            int(s)
            answer = True
        except:
            answer = False
    return answer