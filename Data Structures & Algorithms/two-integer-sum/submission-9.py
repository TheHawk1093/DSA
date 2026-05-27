class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            elem = target - nums[i]
            if elem in nums[i+1:]:
                new = nums[i+1 :]
                j = new.index(elem)
                break
        return [i,j+i+1]