def solution(nums):
    nums.sort()
    ln = len(nums)
    sc = ln*(ln-1)*(ln-2)//6
    for i in range(ln):
        for j in range(i+1, ln):
            for k in range(j+1, ln):
                sm = nums[i]+nums[j]+nums[k]
                dd = 0
                for u in range(2, sm):
                    if sm % u == 0:
                        dd = 1
                sc -= dd  
    answer = sc

    return answer