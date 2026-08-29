class MyHashMap:

    def __init__(self):
       self.mymap = [[] for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        bucket = self.mymap[key % 1000]
        #buckets are an array with key value pairs
        #so outer list[], bucket[], which stores [key, value]  

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i][-1] = value
                print(bucket)
                return
        bucket.append([key,value])

    def get(self, key: int) -> int:
        bucket = self.mymap[key % 1000]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                return bucket[i][-1]
        
        return -1

    def remove(self, key: int) -> None:
        bucket = self.mymap[key % 1000]
        for i in range(len(bucket)):
            a,b = bucket[i]
            if a == key:
                bucket.remove([a,b])
                return
        
    
                    


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)