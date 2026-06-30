class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        mylst = []

        prod = 1
        
        for i in range(len(nums)): 
            for j in range(len(nums)):
 
                if i == j and i == len(nums) - 1: 
                    mylst.append(prod)
                elif i == j: 
                    continue
                else: 
                    prod *= nums[j]
                    print(prod)
                    if j == len(nums) - 1:
                        mylst.append(prod)
                        prod = 1
        
        print(mylst)

        return mylst