def solution(arr):
    answer = []
    a = arr.pop(0)
    answer.append(a)
    for i in arr:
        if i != a:
            answer.append(i)
            a = i
    
    '''
    while len(arr)>0:
            if arr[0] == answer[-1]:
                arr.pop(0)
            else:
                a = arr.pop(0)
                answer.append(a)
    '''            
    return answer