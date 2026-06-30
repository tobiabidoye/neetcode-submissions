class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        max_prod = 0
        r = len(heights) - 1
        while l < r:
            

            while r > l:
                
                #fast right pointer
                width = r - l
                height = min(heights[l],heights[r])
                curr_prod = height * width
                #this is the product
                #decrement fast pointer
                max_prod = max(max_prod, curr_prod)
                r -= 1
            #slow left pointer
            r = len(heights) - 1
            l += 1
        return max_prod

            

                
            


            
  