class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False

        s1Count, s2Count = [0] * 26 , [0] * 26
        #part 1 is getting all values in s1 and all s2 values up to len s1 in the arrays
        #get all values in s1 and then the values of s2 which are the same length as s1 
        for i in range(len(s1)): 
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0

        #checking frequencies of the map
        #part2 first iteration to see if the substring is in the first k (with k being the len of s1) values in s2
        for i in range(26): 
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        if matches == 26: 
            return True

        l = 0 
        for r in range(len(s1), len(s2)):
            if matches == 26: 
                return True

            index = ord(s2[r]) - ord('a')

            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] == s2Count[index] - 1 :
                matches -= 1
           
            
            index2 = ord(s2[l]) - ord('a')
        
            s2Count[index2] -= 1
            if s1Count[index2] == s2Count[index2]:
                matches += 1
            elif s1Count[index2] == s2Count[index2] + 1 :
                matches -= 1

            l += 1

        return matches == 26
        
             
