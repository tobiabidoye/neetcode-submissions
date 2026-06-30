class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        my_map = defaultdict(int) 
        max_rep = 0 
        for r in range(len(s)): 
            #get max character value
            my_map[s[r]] += 1 
            max_val = max(my_map.values()) 

            if((r - l + 1) - max_val <= k): 
                max_rep = max(max_rep, (r - l + 1)) 
                print(f"max replacement currently {max_rep}")

            while ((r - l + 1) - max_val) > k: 
                #remove value from the map and increment left  
                 
                my_map[s[l]] -= 1 
                l += 1
                max_rep = max(max_rep, (r - l + 1))

        return max_rep
        
                
                

