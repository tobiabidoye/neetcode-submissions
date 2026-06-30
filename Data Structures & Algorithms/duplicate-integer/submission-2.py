class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mylst = []

        for i in nums: 
            if i not in mylst: 
                mylst.append(i)
            else:
                return True
        
        return False