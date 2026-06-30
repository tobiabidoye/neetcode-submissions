class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = [(i,j) for i,j in zip(position,speed)]
        print(res)
        res.sort(reverse = True)
        stack = []

        for i, j in res:
            stack.append((target - i)/ j) 
            if len(stack) >= 2 and stack[-1] <= stack[-2]: 
                stack.pop()

        return len(stack)
