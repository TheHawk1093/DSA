class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        op = []
        for i in range(len(nums)):
            left, right = i+1, len(nums) -1
            target = nums[i] * (-1)
            if nums[i] == nums[i-1] and i>0:
                continue
            while left < right:
                if nums[left] + nums[right] == target:
                    ans = [nums[i],nums[left],nums[right]]
                    op.append(ans)
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right +1]:
                        right -= 1

                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return op