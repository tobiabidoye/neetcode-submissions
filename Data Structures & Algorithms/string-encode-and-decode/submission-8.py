class Solution:

    def encode(self, strs: List[str]) -> str:
        mystr = ""

        for i in strs: 
            mystr += i
            mystr += ";"

        self.decode(mystr)
        return mystr 
        
    def decode(self, s: str) -> List[str]:
        myarr = []
        str2 = ""
        for i in s:
            
            if i == ";": 
                myarr.append(str2)
                str2 = ""
            else: 
                str2 += i
        return myarr
