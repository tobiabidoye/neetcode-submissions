class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def split(arr):
            if len(arr) == 1: 
                return arr
            mid = len(arr) // 2
            l = split(arr[0:mid])
            r = split(arr[mid:len(arr)])

            return merge(l,r)

        def merge(arr1, arr2):
            result = []
            count1 = 0
            count2 = 0

            while count1 < len(arr1) and count2 < len(arr2):
                if arr1[count1] < arr2[count2]:
                    result.append(arr1[count1])
                    count1 += 1
                else:
                    result.append(arr2[count2])
                    count2 += 1
            
            if count1 <= len(arr1) - 1:
                result += arr1[count1:]
            else:
                result += arr2[count2:]
            return result
        
        return split(nums)

