class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        myarr = [[] for _ in range(3)]
        for i in range(len(nums)):
            myarr[nums[i]].append(nums[i])
        numsInd = 0
        for i in range(len(myarr)):
            for j in range(len(myarr[i])):
                nums[numsInd] = myarr[i][j] 
                numsInd += 1 
        
        print(nums)