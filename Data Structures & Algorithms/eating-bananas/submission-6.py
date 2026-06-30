class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 
        r = max(piles)

        minimum = 0
        while l <= r: 
            mid = (l + r) // 2

            time = 0 
            for i in range(len(piles)): 
                time += math.ceil(piles[i] / mid)
            
            if time > h: 
                l = mid + 1
            elif time <= h: 
                r = mid - 1
                minimum = mid
        
        return minimum
