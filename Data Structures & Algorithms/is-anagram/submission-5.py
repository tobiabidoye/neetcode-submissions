class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mydict = defaultdict(int)
        cooldict = defaultdict(int)
        for i in s: 
            mydict[i] += 1

        for i in t: 
            cooldict[i] += 1

        if mydict == cooldict: 
            return True
        
        return False
