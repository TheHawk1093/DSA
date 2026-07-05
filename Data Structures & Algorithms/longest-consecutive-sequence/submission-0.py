class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq_map = Counter(nums)
        max_count = 0
        
        for i in range(len(nums)):
            if (nums[i] - 1) not in freq_map:
                count = 0
                num = nums[i]
                while (num) in freq_map:
                    count += 1
                    num += 1
                if count > max_count:
                    max_count = count
            else:
                continue
        
        return max_count