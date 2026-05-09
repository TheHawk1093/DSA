class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        visited = {}
        left = 0
        for right in range(len(s)):
            if s[right] in visited and visited[s[right]] >= left:
                left = visited[s[right]] + 1   # Shifting the start of subarray from left

            visited[s[right]] = right  #updating new position or the letter

            max_len = max(max_len, right - left + 1) #Updating maximum length
        
        return max_len