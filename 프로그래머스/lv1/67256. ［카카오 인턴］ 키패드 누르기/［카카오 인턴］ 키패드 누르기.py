def solution(numbers, hand):
    lh = [3,1]
    rh = [3,1]
    answer = ''
    for n in numbers:
        if n in [1,4,7]:
            answer += 'L'
            #lh = str(n)
            lh = [n//3, 1]
        elif n in [3,6,9]:
            answer += 'R'
            rh = str(n)
            rh = [(n//3)-1, 1]
        else:
            mid = [2, 5, 8, 0]
            mn = mid.index(n)
            ld = abs(mn - lh[0]) + lh[1]
            rd = abs(mn - rh[0]) + rh[1]
            print(n, mn, lh, rh, ld, rd)
            if ld < rd: #왼손 거리가 더 가까우면
                answer += 'L'
                lh = [mn, 0]
            elif rd < ld: #오른손 거리가 더 가까우면
                answer += 'R'
                rh = [mn, 0]
            else: #ld == rd
                if hand == "left":
                    answer += 'L'
                    lh = [mn, 0]
                else:
                    answer += 'R'
                    rh = [mn, 0]
            ld, rd = 0, 0
            # print(ld, rh)     
    return answer