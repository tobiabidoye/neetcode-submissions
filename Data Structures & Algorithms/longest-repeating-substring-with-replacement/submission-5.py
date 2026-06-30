class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen = 0
        l = 0
        mymap = defaultdict(int)

        for r in range(len(s)):  
            #now at this point we can lock in and add stuff to the map
            mymap[s[r]] += 1
            #ensure that the number of strings changed to find max replacements do not exceed k 
            if ((r -l + 1) - max(mymap.values())) > k: 
                mymap[s[l]] -= 1
                l += 1
                continue
        
        return r -l + 1 
        