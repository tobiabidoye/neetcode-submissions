class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right: 
            
            while left < right and not self.alphaNum(s[left]): 
                print(s[left])
                #if left pointer not alphanumeric increment
                left += 1
            
            while left < right and not self.alphaNum(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True

            
            
            
        
    def alphaNum(self, c): 
        #gets ascii representation of the character
        #if alphanumeric return true else return false
        if (ord('A') <= ord(c) <= ord('Z')
        or ord('a') <= ord(c) <= ord('z')
        or ord('0') <= ord(c) <= ord('9')):
            return True
        else: 
            return False