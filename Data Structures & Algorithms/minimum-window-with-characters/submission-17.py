class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): 
            return ""
        if s == t: 
            return s
        map1 = defaultdict(int)
        map2 = defaultdict(int)
        count1 = 0
        count2 = 0
        for i in range(len(t)): 
            map1[t[i]] += 1

        count1 = len(map1) 
        print(count1)
        print(map1)
        l = 0 
        min_len = float('inf')
        mypair = [None, None]
        
        for r in range(len(s)):
            map2[s[r]] += 1
            if s[r] in map1 and map2[s[r]] == map1[s[r]]: 
                count2 += 1       
                    
            while l <= r and count1 == count2:
                
                if(min_len > r-l+1):
                    print("getting accessed 2")
                    min_len = r-l+1
                    mypair = [l,r]

                map2[s[l]] -= 1
                if s[l] in map1:  
                    if map2[s[l]] < map1[s[l]]:  
                        count2 -= 1 
                
                l += 1
                print(l,r)
            
        
      
        print(mypair)
        print(min_len) 
        if mypair == [None, None]:
            return ""
        return (s[mypair[0]: mypair[1] + 1])



        
            
