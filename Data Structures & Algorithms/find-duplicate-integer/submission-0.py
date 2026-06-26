class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_map = {}
        for num in nums:
            if num in hash_map:
                return num
            else:
                hash_map[num] = 1
        
        
         