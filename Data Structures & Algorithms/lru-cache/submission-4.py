class ListNode:
    def __init__(self,key = None,value = None,prev = None,next = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        self.leftNode = ListNode()
        self.rightNode = ListNode()

        self.leftNode.next = self.rightNode
        self.rightNode.prev = self.leftNode

        self.lruCache = {}
        

    def get(self, key: int) -> int:
        if key in self.lruCache:
            oldNode = self.lruCache[key]
            self.remove(oldNode)
            self.add(oldNode)
            return oldNode.value
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key not in self.lruCache:
            newNode = ListNode(key,value,None,None)
            self.add(newNode)
            self.lruCache[key] = newNode
        elif key in self.lruCache:
            oldNode = self.lruCache[key]
            self.remove(oldNode)
            self.add(oldNode)
            oldNode.value = value
            # do i need to reattach oldNode
            self.lruCache[key] = oldNode
        if len(self.lruCache) > self.capacity: # evict
            evict_key = self.leftNode.next.key
            self.remove(self.leftNode.next)
            del self.lruCache[evict_key]

    def add(self,node):
        node.next = self.rightNode
        node.prev = self.rightNode.prev

        self.rightNode.prev.next = node
        self.rightNode.prev = node

    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev


    # hashmap makes get in o of 1, hard to keep track of order and eviction
    # heap of size cap when over cap evict/ pop
    # put is logn and get a random val will be nlogn possibly need to remake tree after getting to expensive
    # hashmap is get and put in o of 1 but order is hard
    # link list order is easy but get is hard, maintain a hashmap and reference the link list

    # the way get works is it should be moved to fron since just got used

    # put should check if exists then update whoch will need remove and add to front

    # both need a remove and add
        
