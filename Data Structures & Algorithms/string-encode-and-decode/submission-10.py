class Solution:

    def encode(self, strs: List[str]) -> str:
        mystr = ""

        for i in strs: 
            mystr += str(len(i))
            mystr += ";"
            mystr += i

        self.decode(mystr)
        return(mystr)
    def decode(self, s: str) -> List[str]:
        lst = []
        i = 0
        while i < len(s): 
            j = i
            while s[j] != ';':
                j+= 1
            length = int(s[i:j])
            i = j+1
            j = i + length
            lst.append(s[i:j]) #append between first letter and before integer
            i = j
        
        return lst
            
