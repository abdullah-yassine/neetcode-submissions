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
        # 1. first pass
        if head is None:
            return None
        old_curr= head
        hashmap = {None:None}
        while old_curr.next:
            hashmap[old_curr] = Node(old_curr.val)
            old_curr= old_curr.next
        hashmap[old_curr] = Node(old_curr.val)
        
        old_curr, new_curr= head, hashmap[head]
        while old_curr:
            new_curr.random = hashmap[old_curr.random]
            new_curr.next = hashmap[old_curr.next]
            old_curr, new_curr = old_curr.next, new_curr.next
        return hashmap[head]