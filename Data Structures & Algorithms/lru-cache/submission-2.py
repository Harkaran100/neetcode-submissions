class ListNode:

    def __init__(self,key,val,prev = None,next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.lruCache = {}
        self.capacity = capacity

        self.left = ListNode(0,0)
        self.right = ListNode(0,0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add(self,node):
        # node pointers
        node.prev = self.right.prev
        node.next = self.right

        # surronding pointers
        self.right.prev.next = node
        self.right.prev = node
        

    def get(self, key: int) -> int:
        if key in self.lruCache:
            get_Node = self.lruCache[key]
            # remove
            self.remove(get_Node)

            # append to right
            self.add(get_Node)

            return get_Node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.lruCache: # new key
            new_Node = ListNode(key,value)
            self.add(new_Node)
            self.lruCache[key] = new_Node
        # update key
        else:
            old_Node = self.lruCache[key]
            old_Node.val = value
            
            self.remove(old_Node)
            self.add(old_Node)
        if len(self.lruCache) > self.capacity:

            del_Key = self.left.next.key
            del self.lruCache[del_Key]
            self.left.next = self.left.next.next
            self.left.next.prev = self.left
        


    # can think of it as a queue, if value is put or get, get from queue and append to end of queue
    # if a new value is put when at capcity last value is evicted
    # however with queue get and update to front will not be o of 1 time 
    # since k:v pair im thinking hashmap
    # however with hashmap how can we maintain a order?

    # doubly link list allows us to put and get in o of 1 but we cant use key to find val or keep size in mind

    # somehow use hashmap and as key store reference to that double link val
        
