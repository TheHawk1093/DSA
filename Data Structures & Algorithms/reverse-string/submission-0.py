class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        n = len(s)//2 if len(s)%2 == 0 else (len(s)//2 + 1)

        for i in range(n):
            s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]