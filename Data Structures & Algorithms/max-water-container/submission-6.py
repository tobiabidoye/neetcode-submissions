class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        
        area = 0
        while l < r: 

            width = r - l 
            height = min(heights[l], heights[r])

            curarea = width * height
            area = max(area, curarea)

            if heights[l] >= heights[r]: 
                r -= 1
                continue
            elif heights[l] <= heights[r]: 
                l += 1
                continue
        
        return area

