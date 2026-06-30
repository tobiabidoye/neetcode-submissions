class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        lboundary = 1
        rboundary = 1

        larr = [1 for i in range(len(nums))]
        rarr = [1 for j in range(len(nums))]

        for i in range(len(nums)):
            larr[i] = lboundary
            lboundary *= nums[i]

        for j in range(len(nums) -1, -1, -1): 
            rarr[j] = rboundary 
            rboundary *= nums[j]

        res =[]

        for i in range(len(nums)): 
            res.append(larr[i] * rarr[i])
        
        return res
             