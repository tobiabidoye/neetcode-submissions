class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set()

        for i in nums: 
            myset.add(i)

        count = 0   
        for i in myset: 

            elem = i - 1
            tempcount = 0
            if elem not in myset:
                #if elem is not in set then it is a start

                item = i
                
                while item in myset: 
                    item += 1
                    tempcount += 1

                if tempcount > count: 
                    count = tempcount

        
        return count