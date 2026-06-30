class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        myset = set()
        l = 0 
        max_count = 0 
        for r in range(len(s)): 
            while s[r] in myset: 
                myset.remove(s[l])
                l += 1
            
            max_count = max(max_count, r - l + 1)
            myset.add(s[r])

        return max_count 