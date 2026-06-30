class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        arr1 = [0] * 26
        arr2 = [0] * 26 
        count = 0
        matches = 0
        #frequency counter?
        for i in range(len(s1)): 
            count += 1 
            arr1[ord(s1[i]) - ord('a')] += 1 
            arr2[ord(s2[i]) - ord('a')] += 1

        
        if arr1 == arr2: 
            return True
        l = 0
        
        #at this point we keep a sliding window
        #fixed window size
        #SLIDIng window only for incrementing and decrementing counts
        #we will compare whole arrays
        for r in range(count, len(s2)):
            if arr1 == arr2: 
                return True
            arr2[ord(s2[r]) - ord('a')] += 1
            arr2[ord(s2[l]) - ord('a')] -= 1
            l+= 1

        if arr1 == arr2: 
            return True
        return False 
            


