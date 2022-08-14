import numpy as np
def solution(participant, completion):
    participant.sort()
    completion.sort()
    ans = participant[-1]
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            ans = participant[i]
            break
    return ans