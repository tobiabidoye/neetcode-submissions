class Solution:

    def encode(self, strs: List[str]) -> str:
        mystr = ""
        for i in strs:
            lenStr = len(i)
            mystr += str(lenStr) + "#"
            mystr += i
        print(mystr)
        return mystr

    def decode(self, s: str) -> List[str]:
        myarr = []
        curStr = ""
        lenStr = ""
        #read up to hash
        #then extract string
        hashFound = False
        countCurStr = 0
        for i in range(len(s)):
            if not hashFound:
                if s[i] != "#":
                    lenStr += s[i]
                else:
                    hashFound = True
                    lenStr = int(lenStr)
                    if lenStr == 0:
                        myarr.append("")
                        hashFound = False
                        lenStr = ""
                    continue
            #now extract string up to lenStr 
            if hashFound:
                curStr += s[i]
                if countCurStr == lenStr - 1:
                    myarr.append(curStr)
                    curStr = ""
                    hashFound = False
                    lenStr = ""
                    countCurStr = 0
                    continue  
                countCurStr += 1
        
                
        return myarr


            
