class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s) - 1
        s2 = s.lower()
        while l < r:
            
            if not s2[l].isalnum():
                #if its not alphaumeric continue
                l += 1
                continue
            elif not s2[r].isalnum(): 
                r -= 1
                continue
            elif s2[r] != s2[l]:
                return False
            
            l += 1
            r -= 1
            
        
        return True




    
         