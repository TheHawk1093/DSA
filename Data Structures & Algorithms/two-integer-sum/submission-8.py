class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in nums:
                j = nums.index(diff)
                
                if i != j:
                    return [i, j]
                
                elif nums.count(diff) > 1:
                    j = nums.index(diff, i + 1)
                    return [i, j]
        return []
