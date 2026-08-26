class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if (len(nums) == 1 and nums[-1] == val) or len(nums) == 0:
            return 0
        
        l = 0
        r = len(nums) - 1
        count = 0
        while l <= r:
            if nums[l] == val and nums[r] != val:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp

            if nums[r] == val:
                r -= 1
            if nums[l] != val:
                l += 1 

        if l != 0:
            return l
        return 0