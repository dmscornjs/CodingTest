def solution(absolutes, signs):
    mn = 0 
    for i in range(len(signs)):
        if signs[i] == False:
            mn += absolutes[i]
    
    answer = sum(absolutes) - 2*mn
    return answer