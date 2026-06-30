class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): 
            return ""
        if s == t: 
            return s
        
        map1 = defaultdict(int)
        map2 = defaultdict(int)
        

        for i in t: 
            map1[i] += 1
            
        count1 = len(map1)
        min_len = float('inf') 
        l = 0
        my_pair = [None, None]
        count2 = 0
        
        for r in range(len(s)): 
            map2[s[r]] += 1
            if s[r] in map1 and map1[s[r]] == map2[s[r]]: 
                count2 += 1
            count = 0
            while l <= r and count2 == count1: 
                count += 1
                print(count)
                if min_len > (r - l + 1): 
                    min_len = r -l + 1
                    my_pair = [l,r]
                
                map2[s[l]] -= 1

                if s[l] in map1 and map2[s[l]] < map1[s[l]]: 
                    count2 -= 1
                print(s[l: r + 1])               
                l += 1  

        if my_pair == [None,None]: 
            return ""

        return s[my_pair[0]: my_pair[1] + 1]
                






            

        