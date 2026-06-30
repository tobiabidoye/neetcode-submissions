class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mylst =[]
        l, r = 0, k - 1

        for i in range(len(nums)): 
            mylst.append(max(nums[l: r + 1]))
            l+= 1
            r += 1
            if r == len(nums): 
                break

        return(mylst)

        
