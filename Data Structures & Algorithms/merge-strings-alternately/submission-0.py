class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l_1, l_2 = len(word1), len(word2)
        merged = ''
        if l_1 > l_2:
            for i in range(l_2):
                merged = merged + word1[i] + word2[i]
            merged = merged + word1[l_2::]
        else:
            for i in range(l_1):
                merged = merged + word1[i] + word2[i]
            merged = merged + word2[l_1:]
        return merged



        