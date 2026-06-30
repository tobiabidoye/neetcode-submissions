class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        curr = [(i,j) for i,j in zip(position, speed)]
        curr.sort(reverse = True)
        stack = []
        print(curr) 
        
        for i, j in curr: 
            stack.append((target - i) / j)

            if len(stack) >= 2 and stack[-1] <= stack[-2]: 
                stack.pop()
        
        return len(stack) 

