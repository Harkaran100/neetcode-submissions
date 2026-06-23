"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 2 pass
        # reason being the random pointer
        # cant do in first pass because the random pointer can point to nodes not yet created

        # first pass to create all copy nodes
        # store in hashmap
        oldToCopy = {None: None}
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy # map
            curr = curr.next
        # hashmap complete

        curr = head
        # 2nd pass add pointers to next and random
        while curr:
            copyNode = oldToCopy[curr]
            copyNode.next = oldToCopy[curr.next]
            copyNode.random = oldToCopy[curr.random]
            curr = curr.next
        return oldToCopy[head]
