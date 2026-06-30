class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = {}

        for i in strs: 
            sortedString = "".join(sorted(i))
            if sortedString not in myMap: 
                myMap[sortedString] = []
            
            myMap[sortedString].append(i)
        
        myLst= []
        for i in myMap:
            myLst.append(myMap[i])

        return myLst 
