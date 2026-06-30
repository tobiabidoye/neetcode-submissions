class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mymap = {}

        for i,j in enumerate(nums):
            mymap[j] = i

        

        for i,j in enumerate(nums): 
            target2 = target - j

            if target2 in mymap and i != mymap[target2]:
                return [i, mymap[target2]]

                
  
        return []
