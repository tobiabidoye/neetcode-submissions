class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1 for i in range(len(nums))]
        postfix = [1 for i in range (len(nums))]

        for i in range(len(nums)): 
            if i == 0: 
                prefix[i] = 1
                continue 
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        print(prefix)

        for i in range(len(nums) -1, -1, -1): 
            if i == len(nums) - 1: 
                postfix[i] = 1
                continue  
            postfix[i] = postfix[i + 1] * nums[i + 1]
                
        print(postfix[i])

        res = []

        for i in range(len(nums)): 
            res.append(prefix[i] * postfix[i])
        
        return res
        