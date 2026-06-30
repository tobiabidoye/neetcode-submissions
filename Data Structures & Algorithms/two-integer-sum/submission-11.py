class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}

        for i,j in enumerate(nums):
            mydict[j] = i

        difference = 0

        for i,j in enumerate(nums): 
            difference = target - j

            if difference in mydict and i != mydict[difference]:
                return[i, mydict[difference]]
            
        return []

