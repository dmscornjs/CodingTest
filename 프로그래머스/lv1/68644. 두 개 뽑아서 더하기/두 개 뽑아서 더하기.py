def solution(numbers):
    li = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            li.append(numbers[i] + numbers[j])
    a = list(set(li))
    a.sort()
    answer = a
    return answer