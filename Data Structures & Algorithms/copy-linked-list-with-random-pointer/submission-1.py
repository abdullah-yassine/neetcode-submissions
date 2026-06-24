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
        new_head = Node(head.val)
        old_curr, new_curr= head, new_head
        hashmap = {None:None}
        while old_curr.next:
            hashmap[old_curr] = new_curr
            new_curr.next = Node(old_curr.next.val)
            old_curr, new_curr = old_curr.next, new_curr.next
        hashmap[old_curr] = new_curr
        new_curr.next = None
        
        old_curr, new_curr= head, new_head
        while old_curr:
            new_curr.random = hashmap[old_curr.random]
            old_curr, new_curr = old_curr.next, new_curr.next
        return new_head