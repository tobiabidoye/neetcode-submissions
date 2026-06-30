class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i,j in enumerate(heights):
            start = i
            while stack and stack[-1][1] > j: 
                index, height = stack.pop()
                max_area = max(max_area, height*(i - index))
                start = index 
            
            stack.append((start, j))
        
        for i , j in stack: 
            max_area = max(max_area, j * (len(heights) - i))
        
        return max_area
            

