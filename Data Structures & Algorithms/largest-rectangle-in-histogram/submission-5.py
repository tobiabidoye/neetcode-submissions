class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        #append both index and height in a pair
        for i, j in enumerate(heights): 
            #this loop should run in o(n) time even though there is an inner loop 
            #amortized time wise it is o(n) because the while loop will ensure popping off the stack of each value only happens once
            #start to always keep track of start index
            start = i 
            while stack and stack[-1][1] > j: 
                index, height = stack.pop()
                max_area = max(max_area, (height *(i - index)))
                start = index   
            stack.append((start, j))


        for i, j in stack: 
            #loop through the stack now
            max_area = max(max_area, (j * (len(heights) - i)))

        return max_area 
