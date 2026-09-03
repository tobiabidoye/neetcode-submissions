class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        low = 0
        mid = 0
        high = len(nums) - 1
        count = 0
        while mid <= high:
            cur = nums[mid]
            if cur == 0: 
                nums[mid] = nums[low]
                nums[low] = cur
                low += 1
                mid += 1
            elif cur == 2:
                nums[mid] = nums[high]
                nums[high] = cur
                high -= 1
            elif cur == 1:
                mid += 1
        print(nums)