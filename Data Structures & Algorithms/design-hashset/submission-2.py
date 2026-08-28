class MyHashSet:

    def __init__(self):
        self.myset = [[] for _ in range(1000)]

    def add(self, key: int) -> None:
        bucket = self.myset[key % 1000] 
        if len(bucket) == 0:
            bucket.append(key)
            return
        elif key not in bucket:
            bucket.append(key)
        
    def remove(self, key: int) -> None:
        bucket = self.myset[key % 1000]
        if len(bucket) == 0 or key not in bucket:
            return
        else:
            bucket.remove(key) 
    def contains(self, key: int) -> bool: 
        bucket = self.myset[key % 1000]
        if key in bucket:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)