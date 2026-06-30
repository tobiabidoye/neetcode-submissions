class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort
        #array with columns initiated to track frequency make it i + 1
        #track frequency with a map

        lst = [[] for i in range(len(nums) + 1)] 
        myMap = defaultdict(int)

        for i in nums: 
            myMap[i] += 1
        
        for i , j in myMap.items(): 
            lst[j].append(i)

        print(lst) 
        res = []

        for i in range(len(lst) -1, -1, -1):  

            for j in lst[i]:    
                res.append(j)

                if len(res) == k: 
                    return res
               
              
        return res
        
         