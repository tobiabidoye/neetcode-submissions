class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) #o(n)

        res = max(piles) #alse o(n)

        while l <= r: 
            m = (l+r) // 2  

            hours = 0

            for i in piles: 
                #hourly eating rate
                hours += math.ceil(i / m)
            
            if hours <= h: 
                res = min(m, res)
                r = m - 1
            else: 
                l = m + 1
        
        return res