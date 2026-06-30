class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortedString = ''.join(sorted(s))
        sortedString2 = ''.join(sorted(t))

        if sortedString == sortedString2: 
            return True
        
        return False