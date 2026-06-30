class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = self.removeAlNum(s)
        lowcase = newString.lower()
        print(lowcase) 
        l = 0
        r = len(lowcase) - 1  
        while(l < r): 

            if lowcase[l] != lowcase[r]: 
                return False
            
            l += 1
            r -= 1
        
        return True

    def removeAlNum(self, text):
        return "".join(filter(str.isalnum, text)) 
