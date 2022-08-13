def solution(n, lost, reserve):
    rs = [] #받을 수 있는 학생
    mr = [] #빌려줄 수 있는 학생
    rv = reserve.copy()
    for i in reserve:
        if i in lost:
            rv.remove(i)
            lost.remove(i)
            #rs.append(i)
            #mr.append(i)
    for i in lost:
        if i+1 in rv:
            #reserve.remove(i)
            rs.append(i)
            mr.append(i+1)
            #lost.remove(i+1)
        if i-1 in rv:
            #reserve.remove(i)
            rs.append(i)
            mr.append(i-1)
            #lost.remove(i-1)
    l = len(lost)
    print(rs, mr)

    answer = n - l + min(len(set(mr)), len(set(rs)))
    return answer