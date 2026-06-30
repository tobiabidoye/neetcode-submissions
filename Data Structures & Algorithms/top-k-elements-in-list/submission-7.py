class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mydict = defaultdict(int)
        myarr = [[] for i in range(len(nums) + 1)]
        print(myarr)

        for i in nums: 
            mydict[i] += 1 

        print(mydict)

        for i,j in mydict.items():
            myarr[j].append(i)
            print(i,j)

        myarr2 = []
        count = 0 
        for i in range(len(myarr) - 1, -1, -1): 
            
            for j in range(len(myarr[i])):
                myarr2.append(myarr[i][j])
                count += 1
                if count == k: 
                    return myarr2
        
        
        


        