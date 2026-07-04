class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Optimal but not clean
        """
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
        """

        # Brute force solution with complexity O(n2)
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return (i,j)
        """
        for i in range(len(nums)):
            num = target - nums[i]
            if num in nums[i+1:]:
                j = nums[i+1:].index(num)
                return [i, i+j+1]
