class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.my_map = OrderedDict() 


    def get(self, key: int) -> int: 
        if key in self.my_map:
            self.my_map.move_to_end(key) 
            return self.my_map[key]
        else: 
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.my_map:
            self.my_map[key] = value    
            self.my_map.move_to_end(key) 
            return 
        if len (self.my_map) == self.capacity:
            #remove least recently used
            self.my_map.popitem(last=False) 
         
        self.my_map[key] = value    
        self.my_map.move_to_end(key) 

        
