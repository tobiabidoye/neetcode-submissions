class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset = set()
        l = 0

        max_len = 0
        for r in range(len(s)): 

            while myset and s[r] in myset: 
                myset.remove(s[l]) 
                l += 1 
                continue

            max_len = max(max_len, r - l + 1)
            myset.add(s[r])


        
        return max_len 
        