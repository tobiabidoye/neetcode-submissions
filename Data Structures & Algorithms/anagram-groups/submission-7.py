class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}

        for i in strs: 
            stringy = ''.join(sorted(i))

            if stringy not in mydict: 
                mydict[stringy] = []
                mydict[stringy].append(i)
            else: 
                mydict[stringy].append(i)
        newArr = [] 
        for i , j in mydict.items(): 
            newArr.append(j)

        print(newArr)
        return newArr
