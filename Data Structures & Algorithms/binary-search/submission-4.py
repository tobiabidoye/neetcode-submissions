class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = 0
        b = len(nums) - 1

        while (a <= b): 
            midpoint = (a+b) // 2
            if(nums[midpoint] < target): 
                a = midpoint + 1
            elif(nums[midpoint] > target): 
                b = midpoint - 1
            else: 
                return midpoint

        return -1
        