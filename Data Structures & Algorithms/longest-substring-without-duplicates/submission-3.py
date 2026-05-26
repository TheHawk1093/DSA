class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Map to store the most recent index of each character
        char_map = {}
        max_len = 0
        left = 0

        for right in range(len(s)):
            # If the character is a duplicate and inside the current window
            if s[right] in char_map and char_map[s[right]] >= left:
                # Move the left pointer past the last seen duplicate
                left = char_map[s[right]] + 1
            
            # Update the character's last seen position
            char_map[s[right]] = right
            
            # Calculate window size and update max length
            max_len = max(max_len, right - left + 1)
            
        return max_len
