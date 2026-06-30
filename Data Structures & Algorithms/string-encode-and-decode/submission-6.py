class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs: 
            res += str(len(i)) + "#" + i
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        j = 0
        i = 0 
        while j < len(s): 
            i = j
            while s[i] != "#": 
                i += 1
            length = int(s[j:i])
            res.append(s[i+1:i+1+length])
            j = i+1+length
        return res