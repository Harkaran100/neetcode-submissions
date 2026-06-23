class Node:
    def __init__(self,key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # hashmap
        self.right = Node(0,0) # MRU
        self.left = Node(0,0) # LRU
        self.left.next = self.right
        self.right.prev = self.left

        
    # helper
    def remove(self, node):
        next = node.next
        prev = node.prev
        prev.next = next
        next.prev = prev
    
    # helper
    def add(self,node):
        prev = self.right.prev
        next = self.right
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev


    def get(self, key: int) -> int:
        if key in self.cache: # check if in cache
            self.remove(self.cache[key])
            self.add(self.cache[key]) # move to mru
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:

        # check if key exist
        if key in self.cache:
            self.remove(self.cache[key])
        # create/ update hashmap of key
        self.cache[key] = Node(key, value)
        self.add(self.cache[key]) # add to mru

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]



# we need a way to figure out which key was LRU, how to keep track of this?
# get and put operations can probably be done in o(1) time in hashmap
# but we cant use hashmap to store key and value because then there is no way to keep track of 
# when something was used
# a doubly link list could be used to determine LRU and MRU
# need to update each time get or set is used
# create helper functions to write clean code for remove and add to doubly link list
# can have value portion of hashmap be pointer to doubly link list value
        


        
