from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        ans = freq.most_common(k)
        res = []
        for num, count in ans:
            res.append(num)
        
        return res

        