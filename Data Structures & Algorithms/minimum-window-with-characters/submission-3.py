class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): 
            return ""


        mydict = defaultdict(int)
        count1 = 0
        dict2 = defaultdict(int)
        count2 = 0

        for i in t: 
            mydict[i] += 1         
            count1 += 1
        
        #loop through first indices

        l = 0
        tracker = 0
        min_count = len(s)
        toreturn = ""
        for r in range(len(s)): 

                if s[r] in mydict: 
                    dict2[s[r]] += 1  
                    if dict2[s[r]] == mydict[s[r]]: 
                        count2 += 1
                    

                #when match is found 
                #how do we store the indices to scan through
                while count2 == len(mydict) and l <= r:
                    print("condition triggered")  

                    if (r - l) < min_count: 
                        print(toreturn)
                        toreturn = s[l: r + 1]
                    min_count = min(min_count, r - l)
                    tracker = r
                    if s[l] in dict2:     
                        print("\n")
                        print("condition2 trigerred")
                        if dict2[s[l]] > 0: 
                            dict2[s[l]] -= 1
                        
                        if dict2[s[l]] < mydict[s[l]]: 
                            count2-= 1
                    l += 1

                
                
            
        return toreturn
        

        