class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        myset = set(nums)

        seq = 0
        for i in myset:
            
            if i - 1 not in myset: 
                cur = 0 
                while (cur + i) in myset: 
                    cur += 1
                print(cur)
                seq = max(seq, cur)

        return seq