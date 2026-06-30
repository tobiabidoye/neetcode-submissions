class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mymap = defaultdict(int)
        map2 = defaultdict(int)

        if(len(s) != len(t)):
            return False 
            
        for i in range(len(s)): 
            mymap[s[i]] += 1
            map2[t[i]] += 1
        
        if mymap == map2: 
            return True
        
        return False