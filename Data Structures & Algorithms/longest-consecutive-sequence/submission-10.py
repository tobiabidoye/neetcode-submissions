class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        mySet = set(nums)
        seq = 0
        for i in mySet: 
            
            if i - 1 not in mySet: 
                curSeq = 0
                while i + curSeq in mySet: 
                    curSeq += 1
                seq = max(seq, curSeq)
        
        return seq 