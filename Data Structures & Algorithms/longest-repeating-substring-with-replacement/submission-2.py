class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxs = 0
        mymap = defaultdict(int)
        count = 0
        for r in range(len(s)): 
            count = r
            mymap[s[r]] += 1
            maxs = max(maxs, max(mymap.values()))
            if ((r - l + 1) - max(mymap.values()))  > k: 
                #increment atp right? 
                #we know at this point we have decremented from the window
                #think when you decrement from the window what do you need to do?
                mymap[s[l]] -= 1
                l += 1
                continue
        return r - l + 1
        
        
            





