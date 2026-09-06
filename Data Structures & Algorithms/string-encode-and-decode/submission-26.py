class Solution:

    def encode(self, strs: List[str]) -> str:
        mystr = ""
        for i in strs:
            lenStr = len(i)
            mystr += str(lenStr) + "#"
            mystr += i
        return mystr

    def decode(self, s: str) -> List[str]:
        myarr = []
        curStr = ""
        lenStr = ""
        #read up to hash
        #then extract string
        hashFound = False
        countCurStr = 0
        i = 0
        while i < (len(s)):
            if not hashFound:
                if s[i] != "#":
                    lenStr += s[i]
                else:
                    hashFound = True
                    print(lenStr)
                    lenStr = int(lenStr)
                    if lenStr == 0:
                        myarr.append("")
                        hashFound = False
                        lenStr = ""
                    i += 1
                    continue
                i += 1
            #now extract string up to lenStr 
            if hashFound:
                myarr.append(s[i:i + lenStr])
                i += lenStr
                lenStr = ""
                hashFound = False
                
        return myarr


            
