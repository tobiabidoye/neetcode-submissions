class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        myset = set(nums)
        
        print(myset)
        
        seq = 0
        for i in myset: 
            
            if i - 1 not in myset:
                currseq = 0
                while(i + currseq) in myset: 
                    currseq += 1
                
                seq = max(seq,currseq)

        return seq

         

