class TimeMap:

    def __init__(self):
        self.mymap = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mymap: 
            self.mymap[key] = []
        self.mymap[key].append((timestamp,value))
        print(self.mymap)

            
    def get(self, key: str, timestamp: int) -> str:
        #binary search through the key value pair
        if key not in self.mymap: 
            return ""
        l = 0
        r = len(self.mymap[key]) - 1 
        
        result = ""
        while l <= r:
            mid = (l + r) //2
            if self.mymap[key][mid][0] <= timestamp:
                result = self.mymap[key][mid][1]
                l = mid + 1 
            elif self.mymap[key][mid][0] > timestamp:
                r = mid - 1 
        return result