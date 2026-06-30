class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right: 

            #first condition check for isalphanum
            while left < right and not self.is_alpha_num(s[left]): 
                left += 1

            while left < right and not self.is_alpha_num(s[right]): 
                right -= 1
            
            #check for equality of left and right

            if (s[left].lower() != s[right].lower()): 
                return False
            left += 1
            right -= 1 
        
        return True


    def is_alpha_num(self, mystr):
        if(ord('A') <= ord(mystr) <= ord('Z') 
        or ord('a') <= ord(mystr) <= ord('z') 
        or ord('0') <= ord(mystr) <= ord('9')):
            return True
        else: 
            return False
             