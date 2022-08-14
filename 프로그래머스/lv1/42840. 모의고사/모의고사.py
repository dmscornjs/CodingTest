def solution(answers):
    sp1 = [1,2,3,4,5]
    sp2 = [2, 1, 2, 3, 2, 4, 2, 5]
    sp3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    c = [0]*3
    for i in range(len(answers)):
        if sp1[((i+1)%5-1)] == answers[i]:
            c[0] +=1      
        if sp2[((i+1)%8-1)] == answers[i]:
            c[1] +=1
        if sp3[((i+1)%10-1)] == answers[i]:
            c[2] +=1
    answer = []
    for i in range(3):
        if c[i] == max(c):
            answer.append(i+1)

    return answer