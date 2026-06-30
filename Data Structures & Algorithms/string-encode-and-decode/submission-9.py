class Solution:

    def encode(self, strs: List[str]) -> str:
        mystr = ""
        for i in strs: 
            mystr+= i
            mystr += ";"

        self.decode(mystr)
        return mystr
    def decode(self, s: str) -> List[str]:
        mylst = []
        
        mystr = "" 
        for i in s: 
            if i == ";": 
                mylst.append(mystr)
                mystr = ""
            else: 
                mystr += i
        return mylst