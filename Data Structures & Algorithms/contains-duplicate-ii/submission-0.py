class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if abs(i-j) <= k and nums[i] == nums[j]:
                    return True
                elif nums[i] != nums[j]:
                    continue
                else:
                    break
        return False
        
            

        