def solution(numbers):
    li = [c for c in range(10)]
    for i in numbers:
        li.remove(i)
    answer = sum(li)
    return answer