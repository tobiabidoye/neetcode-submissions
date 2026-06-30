class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        l = [0 for i in range(len(nums))] 
        r = [0 for i in range(len(nums))]

        lboundary = 1
        rboundary = 1
        for i in range(len(nums)): 
            l[i] = lboundary
            lboundary *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            r[i] = rboundary
            rboundary *= nums[i]

        res = [] 
        for i in range(len(nums)):
            res.append(l[i]* r[i])
        
        return res