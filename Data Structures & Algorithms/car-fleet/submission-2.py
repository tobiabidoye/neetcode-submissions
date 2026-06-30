class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] 
        res = [(i,j) for i,j in zip(position, speed)]
        res.sort(reverse = True)
        print(res) 

        for i , j in res:
            #to get current finishing time
            print(f"i is {i}")
            print(f"j is {j}")
            stack.append((target - i) / j)
            if len(stack) >= 2 and stack [-1] <= stack [-2]:  
                stack.pop()

        return len(stack) 

            