class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        hash_set = {}
        for num in nums:
            if num in hash_set:
                hash_set[num] += 1
            else:
                hash_set[num] = 1
        top_k = sorted(hash_set, key = hash_set.get)[::-1]
        return top_k[0]
        """
        majority_count = 0
        majority = nums[0]
        for num in nums:
            if nums.count(num) > majority_count:
                majority_count = nums.count(num) 
                majority = num
        return majority

