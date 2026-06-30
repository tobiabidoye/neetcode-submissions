class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymap = {}
        arr = []
        for i,j in enumerate(nums): 
            mymap[j] = i 
        print (mymap)
        difference = 0
        #key contains actual number and value contains the index
        for i,j in enumerate(nums):
            difference = target - j
            
            
            if (difference in mymap) and (mymap[difference] != i): 
               return[i, mymap[difference]]
        print(arr)

        return arr

                          
            

