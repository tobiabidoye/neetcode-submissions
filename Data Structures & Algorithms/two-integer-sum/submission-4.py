class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i, j in enumerate(nums):
            ##enumerate keeps track of the index of each element
            #i is the index j is the element
            target2 = target - j
            if target2 in mydict: 
                return[mydict[target2], i]
            mydict[j] = i
        return []
