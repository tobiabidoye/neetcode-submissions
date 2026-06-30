class Solution:

    def encode(self, strs: List[str]) -> str:
        myStr = ""
        for i in strs:
            s = str(len(i)) 
            myStr += s
            myStr += "#"
            myStr += i
        
        print (myStr)
        return myStr

    def decode(self, s: str) -> List[str]:
        l = []
        i = 0

        while i < len(s): 
            j = i
            while s[j] != "#": 
                j += 1
            length = int(s[i:j])
            print(length)
            l.append(s[j + 1: j + 1 + length])
            i = j + 1 + length 

        return l