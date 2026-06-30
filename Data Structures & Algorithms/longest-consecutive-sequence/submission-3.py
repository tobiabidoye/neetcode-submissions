class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        max_count = 0
        
        for i in myset:
            length = 0
            if (i - 1) not in myset: 
                while(i + length) in myset: 
                    length += 1
                max_count = max(length, max_count)
        return max_count
