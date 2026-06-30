class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mydict = defaultdict(int)
        for i in nums: 
            mydict[i] += 1
        for i, j in mydict.items():
            if j > 1: 
                return True
        return False
         