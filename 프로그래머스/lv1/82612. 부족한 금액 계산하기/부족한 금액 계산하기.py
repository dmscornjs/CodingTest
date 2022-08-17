def solution(price, money, count):
    tt = 0
    for i in range(count):
        tt += price*(i+1)
    
    answer = 0
    if tt > money:
        answer = tt - money

    return answer