class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        myqueue = deque()
        output = []
        l = 0
        r = 0 

        while r < len(nums): 
            
            while myqueue and nums[myqueue[-1]] < nums[r]: 
                myqueue.pop()

            myqueue.append(r)
            if myqueue and myqueue[0] < l: 
                myqueue.popleft()

            #if size of window then get maximum
            if (r-l+1) == k:    
                output.append(nums[myqueue[0]])
                l += 1
            r += 1
        
        return output
                
        
