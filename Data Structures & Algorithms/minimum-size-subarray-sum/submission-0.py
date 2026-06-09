import numpy as np
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = np.inf
        i = 0
        tally = 0
        for j in range(len(nums)):
            tally += nums[j]
            while tally >= target:
                min_len = min(min_len, j-i+1)
                tally -= nums[i]
                i += 1
            
        return min_len if min_len != np.inf else 0





