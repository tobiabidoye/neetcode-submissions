class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #sorting list to prevent duplicates
        res = []
       

        for i, j in enumerate(nums): 
           
            l = i + 1
            r = len(nums) - 1
            
            if i != 0 and j == nums[i - 1]: 
                #case of if left neigbor is equivalent to current
                #allows for no duplicates
                continue

            while l < r: 
                summy = nums[i] + nums[l] + nums[r]
                if summy > 0: 
                    r -= 1
                elif summy < 0: 
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r: 
                        l += 1
        return res
                
                
            
                    

        


            
