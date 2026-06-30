class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymap = {}
        for i,j in enumerate(nums): 
            mymap[j] = i       

        difference = 0  

        for i,j in enumerate(nums): 
            difference = target - j
            
            if (difference in mymap) and (mymap[difference] != i): 
                return[i, mymap[difference]]
                