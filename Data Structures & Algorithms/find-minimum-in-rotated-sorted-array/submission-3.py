class Solution:
    def findMin(self, nums: List[int]) -> int:
        #in an n size array rotating the array n times will result in the last n elements being at the front of the array
        #rotating the array a number of times equal to the size of the array will result in the original sorted array

        res = nums[0]

        l = 0
        r = len(nums) - 1

        while l <= r: 

            if nums[l] < nums[r]: 
                res = min(res, nums[l])
                break
            
            m = (l+r) // 2
            res = min(nums[m], res)
            if nums[m] >= nums[l]: 
                l = m + 1
            elif nums[m] <= nums[r]: 
                r = m - 1
        
        return res
            
        
        