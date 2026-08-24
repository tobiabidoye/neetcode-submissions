class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymap = {}

        for i in range(len(nums)):
            temp = nums[i]
            mymap[temp] = i 
        
        for i in range(len(nums)):
            newTarget = target - nums[i]

            if newTarget in mymap and mymap[newTarget] != i:
                lst = []
                lst.append(i)
                lst.append(mymap[newTarget])
                return lst

        return [] 

