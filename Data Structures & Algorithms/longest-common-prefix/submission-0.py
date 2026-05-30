class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = min(strs, key=len)
        for word in strs:
            for i in range(len(common_prefix)):
                if common_prefix[i] == word[i]:
                    continue
                else:
                    common_prefix = common_prefix[:i]
                    break


        return common_prefix if common_prefix else ""
                    
        