class TimeMap:

    def __init__(self):
        self.mymap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mymap:
            self.mymap[key] = []
        
        self.mymap[key].append((value, timestamp))
        print(self.mymap)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mymap: 
            return "" 
        l = 0
        r = len(self.mymap[key]) - 1 
        newstr = ""
        #self.mymap[key][mid][1] <= timestamp
        while l <= r: 
            mid = (l + r) // 2
            if self.mymap[key][mid][1] <= timestamp: 
                newstr=(self.mymap[key][mid][0])
                l = mid + 1
            else: 
                r = mid - 1
        return newstr
        


