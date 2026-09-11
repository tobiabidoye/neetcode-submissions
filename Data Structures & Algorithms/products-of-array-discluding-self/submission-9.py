class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forwardArr = []
        backwardArr = [0 for _ in range(len(nums))]

        forwardProd = 1
        backwardProd = 1
        for i in range(len(nums)):
            forwardProd *= nums[i]
            forwardArr.append(forwardProd) 
        
        for j in range(len(nums) - 1, -1, -1):
            backwardProd *= nums[j]
            backwardArr[j] = backwardProd 

        res = []
        for i in range(len(nums)):
            forward = 1
            backward = 1

            if i > 0:
                forward = forwardArr[i - 1]
            if i < len(nums) - 1:
                backward = backwardArr[i + 1]
            res.append(forward * backward) 

        return res
            
