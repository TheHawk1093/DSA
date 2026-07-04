class Solution(object):
    def hasDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # M1 Hash Map
        """
        duplicate = {}

        for elem in nums:
            if elem in duplicate:
                return True
            else:
                duplicate[elem] = 1
        return False
        """
        # M2 - Set and List length check
        if len(set(nums)) != len(nums):
            return True
        else:
            return False
        
        


        