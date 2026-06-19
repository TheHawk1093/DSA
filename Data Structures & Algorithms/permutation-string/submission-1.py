class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = {}
        for ch in s1:
            if ch in counter:
                counter[ch] += 1
            else:
                counter[ch] = 1
        
        i, j = 0, len(s1) - 1
        counter_s2 = {}
        for elem in s2[i:j+1]:
                if elem in counter_s2:
                    counter_s2[elem] += 1
                else:
                    counter_s2[elem] = 1

        while j < len(s2) -1:
            if counter_s2 == counter:
                return True
            else:
                counter_s2[s2[i]] -= 1
                if counter_s2[s2[i]] == 0:
                   del counter_s2[s2[i]]
                i += 1
                j += 1

                if s2[j] in counter_s2:
                    counter_s2[s2[j]] +=1
                else:
                    counter_s2[s2[j]] = 1
                    
        if counter == counter_s2:
            return True
            

        return False



    
        