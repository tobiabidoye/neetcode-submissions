class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        my_set = set()
        max_len = 0
        for r in range(len(s)): 
            
            while s[r] in my_set: 
                my_set.remove(s[l]) 
                l += 1
            my_set.add(s[r]) 
            max_len = max(max_len, r - l + 1)  
                #increment left
        return max_len 
