class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mymap = defaultdict(int)

        for i in nums:
            mymap[i] += 1
        maxNum = 0
        for i,j in mymap.items():
            maxNum = max(maxNum, j)
        #initialize array with largest element being maxNum 
        myarr = [[]for _ in range(maxNum)]
        for i,j in mymap.items():
            myarr[j-1].append(i)
        print(myarr)
        resArr = []
        for i in range(len(myarr) - 1, -1, -1):
            if len(resArr) == k:
                return resArr
            else:
                resArr.extend(myarr[i])
        
        return resArr

            