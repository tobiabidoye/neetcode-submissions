class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mymap = defaultdict(int)
        myLst = [[] for i in range(len(nums) + 1)]#initialize columns
        for i in nums: 
            mymap[i] += 1

        #append items in map to frequeuncy counting list       
        for i , j in mymap.items(): 
            myLst[j].append(i)

        print(myLst)
        res = [] 
        for i in range(len(myLst) - 1, -1, -1):
            if len(res) == k: 
                break
            
            for j in myLst[i]: 
                res.append(j)
            

        return res


        
       