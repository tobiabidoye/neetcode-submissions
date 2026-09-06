class Solution:

    def encode(self, strs: List[str]) -> str:
        mystr = ""
        for i in strs:
            mystr += i
            mystr += "ç"
        print(mystr)
        return mystr

    def decode(self, s: str) -> List[str]:
        myarr = []

        curStr = ""
        for i in range(len(s)):
            if s[i] != "ç":
                curStr += s[i]
            else:
                myarr.append(curStr)
                curStr = ""
        print(myarr)
        return myarr
            
        
