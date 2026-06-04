class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[write] = nums[i+1]
                write += 1
        return write
        


        
