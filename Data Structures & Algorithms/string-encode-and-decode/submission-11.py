class Solution:

    def encode(self, strs: List[str]) -> str:
        mystr = ""
        for i in strs:
            mystr += str(len(i)) + ";" + i

        self.decode(mystr)
        return mystr

    def decode(self, s: str) -> List[str]:
        i = 0
        mylst = []
        while i < len(s): 
            j = i
            while s[j] != ";": 
                j += 1

            length = int(s[i:j])
            i = j + 1
            j = i + length
            mylst.append(s[i:j])
            i = j
             
        return mylst
