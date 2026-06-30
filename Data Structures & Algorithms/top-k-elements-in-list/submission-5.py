class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #count frequency number appears in array
        #append those frequencies to a 2d array
        #loop from end of array up to k to get the top k frequent elements

        myarr = [[] for i in range (len(nums) + 1) ]
        mymap = defaultdict(int)
        
        for i in nums: 
            mymap[i] += 1
        
        for i,j in mymap.items():
            #for item and frequency 
            #we map each item to the frequency it appears in the hashmap 
            myarr[j].append(i)

        arr2 = []
        count = 0
        for i in range(len(myarr) -1, -1, -1): 
            for j in myarr[i]: 
                arr2.append(j)
                count += 1
                if count == k: 
                    return arr2

        return []