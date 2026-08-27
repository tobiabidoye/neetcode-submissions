class MyHashSet:

    def __init__(self):
        self.myset = []

    def add(self, key: int) -> None:
        if key not in self.myset:
            self.myset.append(key)
        else:
            return

    def remove(self, key: int) -> None:
        if key in self.myset: 
            self.myset.remove(key)
        else:
            return

    def contains(self, key: int) -> bool:
        if key in self.myset:
            return True
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)