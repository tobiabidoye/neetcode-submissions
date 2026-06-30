class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = 0
        b = len(nums) - 1

        while(a <= b): 
            mid = (a+b)//2

            if nums[mid] < target: 
                a = mid + 1
            elif nums[mid] > target: 
                b = mid - 1
            else: 
                return mid
        
        return -1