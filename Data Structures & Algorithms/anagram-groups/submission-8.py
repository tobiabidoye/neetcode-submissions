import string 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map2 = {}
        for i in range(len(strs)):
            map1 = {ch: 0 for ch in string.ascii_lowercase}
            for j in strs[i]:
                map1[j] += 1
            tempLst = []
            for key, val in map1.items():
                tempLst.append((key,val))

            mytuple = tuple(tempLst)
            if mytuple not in map2:
                map2[mytuple] = []
            map2[mytuple].append(strs[i])
            

        toReturn = []
        for i,j in map2.items():
            toReturn.append(j)
        
        return toReturn
