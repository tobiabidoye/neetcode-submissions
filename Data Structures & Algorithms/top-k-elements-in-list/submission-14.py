class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mymap = defaultdict(int)

        for i in nums:
            mymap[i] += 1
        maxim = 0 
        for i,j in mymap.items():
            maxim = max(maxim,j)
        arr = [[] for _ in range(maxim)]
        print(arr)
        for i,j in mymap.items():
            arr[j-1].append(i)
        print(arr)
        toreturn = []
        for i in range(len(arr) - 1,-1,-1):
            if len(toreturn) == k:
                return toreturn
            if len(arr[i]) > 0:
                toreturn.extend(arr[i])
        return toreturn
        
        

            
            
