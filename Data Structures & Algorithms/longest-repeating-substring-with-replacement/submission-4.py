class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        mymap = defaultdict(int)

        for r in range(len(s)): 
            mymap[s[r]] += 1

            if ((r - l + 1) - max(mymap.values())) > k:
                #means you can replace more than k characters
                mymap[s[l]] -= 1
                l += 1
                continue

        return (r - l + 1)
