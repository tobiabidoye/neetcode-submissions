class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = defaultdict(int)
        myarr = [[] for i in range(len(nums) + 1)]

        for i in nums: 
            mydict[i] += 1

        for i, j in mydict.items(): 
            myarr[j].append(i)

        


        count = 0
        arr2 = []

                
        for i in range(len(myarr) - 1, -1, -1):
            for j in myarr[i]: 
                arr2.append(j)
                count += 1
                if count == k: 
                    return arr2
        
        return []
    


