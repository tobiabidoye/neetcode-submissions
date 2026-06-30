class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        #a would be the value, i would be the index
        for i, a in enumerate(nums):
            print(a)
            if i != 0 and a == nums[i-1]: 
                continue 

            l = i + 1
            r = len(nums) - 1
            while l < r: 
                summa = a + nums[l] + nums[r] 

                if summa > 0: 
                    r -= 1
                elif summa < 0: 
                    l += 1
                else: 
                    res.append([a, nums[l], nums[r]])
                
                    l += 1
                    while l < r and nums[l] == nums[l - 1]: 
                        l += 1
                    
        return res 
         


                
