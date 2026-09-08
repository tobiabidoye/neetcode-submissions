class Solution:

    def encode(self, strs: List[str]) -> str:
        #for each string in list
        #concatenate them and add the number with a hash beforehand
        #5#apple
        curStr = ""
        for string in strs:
            lenny = len(string)
            curStr += str(lenny) + "#" + string
        return curStr
    def decode(self, s: str) -> List[str]:
        #now at this point scan through the string
        #read up to the # and then read up to the length of the string and put it in an array
        arr = []
        cur = 0
        lenny = ""
        hashFound = False
        print(s)
        print(arr)
        countEmpty = 0
        while cur < len(s): 
            if not hashFound:
                if s[cur] == "#":
                    hashFound = True
                    lenny = int(lenny)
                    if lenny == 0:
                        print(f"arr append{countEmpty}")
                        arr.append("")
                        countEmpty += 1
                        lenny = ""
                        hashFound = False
                else: 
                    lenny += s[cur]
                cur += 1
                continue
            else:  
                print("triggering")
                arr.append(s[cur:cur + lenny]) 
                cur += lenny
                hashFound = False
                lenny = ""
        return arr 
                

        