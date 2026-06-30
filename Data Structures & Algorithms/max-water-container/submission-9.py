class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxxy = 0
        while l < r: 
            curMax = (r - l) * min(heights[l], heights[r])    
            maxxy = max(curMax, maxxy)
            if heights[l] < heights[r]: 
                l += 1
                continue
            elif heights[r] < heights[l]: 
                r -= 1
                continue
            else: 
                l += 1
                r-= 1
        
        print(maxxy)
        return maxxy

