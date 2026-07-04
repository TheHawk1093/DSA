from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        factor = len(nums)//3
        res = []
        freq = Counter(nums)
        all_pairs = freq.items()
        for item, count in all_pairs:
            if count > factor:
                res.append(item)
        return res

        