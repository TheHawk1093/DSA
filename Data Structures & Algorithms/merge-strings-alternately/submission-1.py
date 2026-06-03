class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l_1, l_2 = len(word1), len(word2)
        result = []
        if l_1 > l_2:
            for i in range(l_2):
                result.append(word1[i])
                result.append(word2[i])
            for letter in word1[l_2::]:
                result.append(letter)
        else:
            for i in range(l_1):
                result.append(word1[i])
                result.append(word2[i])
            for letter in word2[l_1::]:
                result.append(letter)
        return "".join(result)



        