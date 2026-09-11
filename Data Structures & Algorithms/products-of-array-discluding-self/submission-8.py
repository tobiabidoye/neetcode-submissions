class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forwardPrefix = []
        backwardPrefix = [0 for _ in range(len(nums))]
        firstSum = 1
        secondSum = 1
        for i in range(len(nums)):
            firstSum *= nums[i]
            forwardPrefix.append(firstSum)
        for i in range(len(nums) - 1, -1, -1):
            secondSum *= nums[i]
            backwardPrefix[i] = secondSum
        
        res = [0 for _ in range(len(nums))]

        for i in range(len(res)):
            forward = 1
            backward = 1
            if i < len(nums) - 1:
                backward = backwardPrefix[i + 1]
            if i > 0:
                forward = forwardPrefix[i - 1]

            res[i] = forward * backward
        
        return res