class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        longest_seq = 0

        for i in nums:
            if(i - 1) not in nums: 
                #if previous index is not in nums it is the start of a sequence
                length = 0
                while(i + length) in nums:
                    length += 1
                longest_seq = max(length, longest_seq)

        return longest_seq 
