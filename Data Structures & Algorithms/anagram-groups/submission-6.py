class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mydict = {}

        for i in strs: 
            x = ''.join(sorted(i))

            if x in mydict: 
                mydict[x].append(i)
            else: 
                mydict[x] = []
                mydict[x].append(i)

        
        mylst = []
        for i in mydict:
            mylst.append(mydict[i])
        
        return mylst

           
    

        
