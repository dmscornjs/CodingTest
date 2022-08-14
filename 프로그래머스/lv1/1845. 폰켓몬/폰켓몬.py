import numpy as np
def solution(nums):
    m = len(nums)//2
    nu = np.unique(nums)

    answer = min(m, len(nu))
    return answer