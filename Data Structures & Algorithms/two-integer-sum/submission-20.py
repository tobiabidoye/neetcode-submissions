class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymap = {}

        for i, j in enumerate(nums): 
            mymap[j] = i 
            #i is index j is value

        for i,j in enumerate(nums): 
            difference = target - j

            if difference in mymap and i != mymap[difference]:  
               return [i, mymap[difference]]

        return [] 
            

