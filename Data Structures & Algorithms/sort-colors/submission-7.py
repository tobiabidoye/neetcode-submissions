class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mid = 0
        l = 0
        r = len(nums) - 1

        while mid <= r: 
            cur = nums[mid]

            if cur == 0:
                nums[mid] = nums[l] 
                nums[l] = cur
                l += 1
                mid += 1
            elif cur == 2:
                nums[mid] = nums[r]
                nums[r] = cur
                r -= 1
            elif cur == 1:
                mid += 1
        
        print(nums)
         