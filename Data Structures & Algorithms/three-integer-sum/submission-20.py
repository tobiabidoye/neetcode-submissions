class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        for i, j in enumerate(nums): 
            
            
            if i != 0 and j == nums[i - 1]: 
                continue

            l = i + 1
            r = len(nums) - 1 

            while l < r: 

                summa = j + nums[l] + nums[r]
                print(summa)
                if summa > 0: 
                    r-=1
                elif summa < 0: 
                    l+= 1
                else: 
                    
                    res.append([j, nums[l], nums[r]])

                    l += 1
                    while l < r and nums[l] == nums[l-1]: 
                        l += 1
                
        return res
