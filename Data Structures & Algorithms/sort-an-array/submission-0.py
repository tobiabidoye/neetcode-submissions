class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def split(arr: List[int]):
            if len(arr) == 1: 
                return arr
            mid = len(arr) // 2
            l = split(arr[0:mid])
            r = split(arr[mid:len(arr)])
            #after splitting then you merge  
            return merge(l,r)
            
        def merge(a: List[int], b: List[int]) -> List[int]:
            count1 = 0
            count2 = 0
            newLst = []
            while count1 < len(a) and count2 < len(b):
                if a[count1] < b[count2]:
                    newLst.append(a[count1])
                    count1 += 1
                else:
                    newLst.append(b[count2])
                    count2 += 1
            if count1 <= len(a)-1:
                newLst += a[count1:]
            else:
                newLst += b[count2:]

            return newLst
        return split(nums)

            