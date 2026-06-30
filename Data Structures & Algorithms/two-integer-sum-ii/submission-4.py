class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers) - 1

        while l < r:
            summa = numbers[l] + numbers[r]

            if summa > target: 
                r -= 1
                continue
            elif summa < target: 
                l += 1
                continue
            elif summa == target: 
                return [l+1, r+1]

        return []
            

