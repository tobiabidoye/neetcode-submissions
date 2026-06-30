class Solution:

    def encode(self, strs: List[str]) -> str:
        wordstore = ""

        for i in strs: 
            wordstore += str(len(i))
            wordstore += ":"
            wordstore += i
        
        print(wordstore)
        return wordstore 



    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s): 
            j = i

            while s[j] != ":": 
                j += 1

            length = int(s[i:j])
            mystr = s[j + 1 : j + 1 +length]
            res.append(mystr)
            
            i = j  + 1  + length

        return res