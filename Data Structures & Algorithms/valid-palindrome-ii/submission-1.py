class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        left, right = 0, len(s) - 1
        Flag = True
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue
            else:
                s_1 = s[:left] + s[left+1:]
                s_2 = s[:right] + s[right + 1:]
                Flag = False
                break
        
        if Flag:
            return True
        
        left_1, right_1 = 0, len(s_1) - 1
        left_2, right_2 = 0, len(s_2) - 1

        Flag_1 = True
        Flag_2 = True

        while left_1 <= right_1:
            if s_1[left_1] == s_1[right_1]:
                left_1 += 1
                right_1 -= 1
                continue
            else:
                Flag_1 = False
                break
        
        while left_2 <= right_2:
            if s_2[left_2] == s_2[right_2]:
                left_2 += 1
                right_2 -= 1
                continue
            else:
                Flag_2 = False
                break
        
        if Flag_1 or Flag_2:
            return True
        else:
            return False
        """

        def is_palindrome(s:str, left:int, right:int) -> bool:
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                    continue
                else:
                    return False
            return True
        
        left, right = 0, len(s)-1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue
            else:
                return is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1)
                
        return True
        
        


        



        
        