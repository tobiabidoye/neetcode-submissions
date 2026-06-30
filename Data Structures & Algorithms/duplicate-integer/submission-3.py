class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset = set()

        for i in nums: 
            myset.add(i)
        
        if(len(nums) != len(myset)):
            return True
        return False
        