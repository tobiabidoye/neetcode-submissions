class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        max_prod = 0
        r = len(heights) - 1
        while l < r:
            

            
                
            #fast right pointer
            width = r - l
            height = min(heights[l],heights[r])
            curr_prod = height * width
            #this is the product
            #decrement fast pointer
            max_prod = max(max_prod, curr_prod)
            if(heights[l] <= heights[r]):
                l += 1
            else:
                r -= 1
            
            
        return max_prod

            

                
            


            
  