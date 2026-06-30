class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = defaultdict(list)
        mylst = []
        if len(strs) == 1: 
            mylst.append(strs)
            return mylst
        
        for i in strs: 
            mystr = ''.join(sorted(i))
            mydict[mystr].append(i)
            ##counting frequency based on if the sorted frequency matches

        for i, j in mydict.items(): 
            mylst.append(j)
         
        return mylst



        
       

        
       



