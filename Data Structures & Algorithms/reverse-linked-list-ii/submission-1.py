# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        # find the point before the starting point using dummy node
        dummy = ListNode(next=head)
        prev_left = dummy
        for _ in range(left - 1):
            prev_left = prev_left.next
        tail = prev_left.next
        curr, prev = tail, None
        
        for _ in range(right - left + 1): # reverse
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # reconnect after the loop
        prev_left.next = prev
        tail.next = curr
        return dummy.next
        
