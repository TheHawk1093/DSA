class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if abs(i-j) <= k and nums[i] == nums[j]:
                    return True
                elif nums[i] != nums[j]:
                    continue
                else:
                    break
        return False
        """
        data = {}
        for i in range(len(nums)):
            key = nums[i]
            if key in data:
                if abs(data[key] - i) <= k:
                    return True
                else:
                    data[key] = i
            else:
                data[key] = i
        return False
        
        
            

        