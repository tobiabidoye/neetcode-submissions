class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mymap = {}

        for i in strs: 
            sorty = ''.join(sorted(i))

            if sorty in mymap: 
                mymap[sorty].append(i)
            else:
                mymap[sorty] = []
                mymap[sorty].append(i)
        print(mymap)
        mylst = []

        for i,j in mymap.items(): 
            mylst.append(j)
        
        return mylst