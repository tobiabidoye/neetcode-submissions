class Solution:

    def encode(self, strs: List[str]) -> str:
        mystr = ""

        for i in strs: 
            mystr += i
            mystr += "-"

        print(mystr) 
        return mystr


    def decode(self, s: str) -> List[str]:
        myLst = [] 
        wordStore = ""
        for i in s: 
            if i == "-":
                myLst.append(wordStore)
                wordStore = ""
                continue
            wordStore += i
        return myLst