class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] == val and nums[r] != val:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                r -= 1
            
            if nums[r] == val:
                r -= 1
            if nums[l] != val:
                l += 1
        
        return l