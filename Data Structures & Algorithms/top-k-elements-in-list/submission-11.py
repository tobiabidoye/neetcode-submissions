class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mylst = [[] for i in range(len(nums) + 1)]
        mymap = defaultdict(int)

        for i in nums: 
            mymap[i] += 1

        for i ,j in mymap.items(): 
            print(i)
            print(j)
            mylst[j].append(i)

        res = []

        for i in range(len(mylst) - 1, -1, -1): 
            for j in mylst[i]: 
                res.append(j)
                if len(res) == k: 
                    return res