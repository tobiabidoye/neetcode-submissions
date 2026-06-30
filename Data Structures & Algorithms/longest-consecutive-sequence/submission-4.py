class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        myset = set()


        for i in nums: 
            myset.add(i)

        print(myset)
        count = 0
        for i in myset: 
            temp = 0
            tempcount = 0
            if(i - 1) not in myset: 
                temp = i
                while (temp) in myset: 
                    tempcount += 1
                    temp += 1
                if tempcount > count:
                    count = tempcount
        return count 
                 


        

