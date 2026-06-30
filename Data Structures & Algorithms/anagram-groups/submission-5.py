class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        myarr = []
        mymap = {}

        for i in strs: 
            sorty = ''.join(sorted(i))
            if sorty in mymap: 
                mymap[sorty].append(i)
            else: 
                mymap[sorty] = []
                mymap[sorty].append(i)
        print(mymap) 
        for i in mymap:
            myarr.append(mymap[i])

        print(myarr)

        return myarr
        