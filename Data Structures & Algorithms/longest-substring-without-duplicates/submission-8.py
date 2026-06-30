class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0 
        l = 0
        myset = set()

        for r in range(len(s)): 

            #check if item exists in the set
            while s[r] in myset and l < r: 
                myset.remove(s[l])
                l += 1
                continue
            myset.add(s[r])
            cur_len = r - l + 1
            max_len = max(max_len, cur_len)
        
        return max_len