class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forwardArr = []
        backwardArr = [0 for _ in range(len(nums))]
        cur1 = 1
        for i in range(len(nums)):
            cur1 *= nums[i]
            forwardArr.append(cur1)
        cur2 = 1
        for i in range(len(nums) - 1, -1, -1):
            cur2 *= nums[i]
            backwardArr[i] = cur2
        
        res = []
        for i in range(len(nums)):
            cur1 = 1
            cur2 = 1

            if (i - 1) >= 0:
                cur1 = forwardArr[i-1]
            if (i + 1) <= len(nums)-1:
                cur2 = backwardArr[i+1]
            res.append(cur1 * cur2)

        return res 

