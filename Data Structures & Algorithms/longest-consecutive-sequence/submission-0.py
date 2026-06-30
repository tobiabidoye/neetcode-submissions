class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count = 0
        myset = set(nums)
        count = 0
        for i in nums: 
            count = 0
            curr = i
            #o(n) loop
            while curr in myset: 
                #o(n) loop for set
                count += 1
                curr += 1
            
            max_count = max(max_count, count)
        
        return max_count

