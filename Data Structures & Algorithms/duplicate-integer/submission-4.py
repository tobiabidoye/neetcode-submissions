class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset = set()

        #if there is a dupe return true else return false
        #sets do not accept duplicates
        #so if the size of the set is less than size of array return true
        #else return false

        for i in nums: 
            myset.add(i)

        if len(myset) != len(nums): 
            return True
        
        return False