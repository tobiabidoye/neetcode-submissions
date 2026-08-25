class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cur = strs[0] 
        for i in range(len(strs)): 
            temp = cur
            cur = ""
            for j in (range(len(strs[i]))):
                newString = strs[i]
                if j < len(temp) and newString[j] == temp[j]:
                    cur += newString[j]
                elif cur == "":
                    return ""
                else:
                    break
        
        return cur
                