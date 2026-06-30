class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        myarr = [1] * (2 *len(nums)) 
        print(myarr)
        n = len(nums)
        for i in range(len(nums)): 
            myarr[i] = nums[i] 
            myarr[i + n] = nums[i]

        return myarr 