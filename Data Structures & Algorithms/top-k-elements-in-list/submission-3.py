class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = defaultdict(int)
        myarr = [[] for i in range(len(nums) + 1)]

        for i in nums: 
            mydict[i] += 1

        print(mydict)
        print(myarr)
        for i,j in mydict.items(): 
            myarr[j].append(i)

        lst2 = []
        count = 0
        for i in range(len(nums), -1, -1): 
            for j in myarr[i]: 
                lst2.append(j)
                count += 1

                if(count == k):
                    return lst2
        
        print(lst2)
