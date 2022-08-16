def solution(num):
    c = -1
    answer = 0
    for i in range(501):
        if num == 1:
            answer = i
            break
            
        elif i == 500:
            answer = -1

        elif num %2 == 0:
            num = num//2
        else:
            num = num *3 +1
        
    return answer