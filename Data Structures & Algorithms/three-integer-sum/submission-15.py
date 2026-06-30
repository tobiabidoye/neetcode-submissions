class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        myarr = []
        nums.sort()
        for i in range(len(nums)): 

            if nums[i] > 0:
                #if sorted and first index already greater than zero
                #return an empty array as nothing sums to zero 
                break
            if i > 0 and nums[i] == nums[i-1]: 
                #in case of duplicates continue
                continue
            
            
            l = i + 1
            r = len(nums) - 1

            while l < r: 
                summa = nums[l] + nums[r] + nums[i]

                if summa == 0: 
                    myarr.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l-1]: 
                        l += 1
                    
                    while l < r and nums[r] == nums[r + 1]: 
                        r -= 1

                elif summa > 0:
                    r -= 1
                elif summa < 0: 
                    l += 1
        
        return myarr
            

        


