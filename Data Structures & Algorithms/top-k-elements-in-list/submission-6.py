class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mymap = defaultdict(int)
        mylst = [[] for i in range (len(nums) + 1)]
        
        for i in nums: 
            mymap[i] += 1

        for i,j in mymap.items(): 
            mylst[j].append(i)
        count = 0
        lst2 = [] 
        for i in range(len(mylst) -1, -1, -1): 
            for j in mylst[i]:
                lst2.append(j)
                count += 1
                if count == k: 
                    return lst2
        return lst2
    
