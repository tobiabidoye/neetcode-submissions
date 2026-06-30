class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lboundary = 1
        rboundary = 1
        larr = [0 for i in range (len(nums))]
        rarr = [0 for i in range (len(nums))]

        for i in range(len(nums)): 
            larr[i]= lboundary
            lboundary *= nums[i]
        
        print(larr)

        for j in range(len(nums) - 1, - 1, -1): 
            rarr[j] = rboundary
            rboundary *= nums[j]

        print(rarr)
        res = []
        for i in range(len(nums)):
            res.append(larr[i] * rarr[i])

        print(res)

        return res