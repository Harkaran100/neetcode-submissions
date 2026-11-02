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
        

    def get(self, key: int) -> int:
        if key in self.lruCache:
            get_Node = self.lruCache[key]

            # remove from curr location
            get_Node.prev.next = get_Node.next
            get_Node.next.prev = get_Node.prev

            # Append to right
            get_Node.next = self.right
            get_Node.prev = self.right.prev

            # update pointers at right
            self.right.prev.next = get_Node
            self.right.prev = get_Node

            return get_Node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.lruCache: # new key
            new_Node = ListNode(key,value,self.right.prev,self.right)
            self.right.prev.next = new_Node
            self.right.prev = new_Node
            self.lruCache[key] = new_Node
        # update key
        else:

            old_Node = self.lruCache[key]
            old_Node.val = value
            old_Node.prev.next = old_Node.next
            old_Node.next.prev = old_Node.prev

            old_Node.prev = self.right.prev
            old_Node.next = self.right

            self.right.prev.next = old_Node
            self.right.prev = old_Node
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
        
