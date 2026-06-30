class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        longest_seq = 0

        for n in nums: 
            if (n-1) not in myset:
                #in this case it is a start of a sequence
                length = 0
                while (n+length) in myset: 
                    length += 1
                longest_seq = max(length,longest_seq)
        return longest_seq



        