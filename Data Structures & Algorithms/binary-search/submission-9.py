class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = 0
        b = len(nums) - 1

        while a <= b: 
            m = (a+b) // 2

            if(nums[m] > target): 
                b = m - 1
            elif(nums[m] < target):
                a = m + 1
            else: 
                return m 
        
        return -1