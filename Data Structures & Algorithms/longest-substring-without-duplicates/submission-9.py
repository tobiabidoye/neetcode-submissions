class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0 
        myset = set()
        for r in range(len(s)):
            while s[r] in myset:
                myset.remove(s[l])
                l += 1

            #valid length
            max_len = max(max_len, r - l + 1) 
            myset.add(s[r])
        
        return max_len 
