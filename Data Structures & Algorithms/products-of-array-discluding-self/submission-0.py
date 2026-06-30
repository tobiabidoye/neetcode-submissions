class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = [1 for i in range(len(nums) - 1)]
        output = []
        for i in range(len(nums)): 
            if(i == 0): 
                prefix.append(1)
            else: 
                prefix.append(nums[i - 1] * prefix[i - 1])
        
        for i in range(len(nums) - 1, -1, -1): 
            if(i == len(nums) - 1): 
                postfix.append(1)
            else: 
                postfix[i] = (nums[i + 1] * postfix[i + 1])

        for i in range(len(prefix)): 
            output.append(prefix[i] * postfix[i])

        return output
             


        