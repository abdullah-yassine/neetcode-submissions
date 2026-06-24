# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_ptr, l2_ptr = l1, l2
        carry = 0
        new_head = new_ptr = ListNode()
        while l1_ptr or l2_ptr:
            two_sum = (l1_ptr.val if l1_ptr else 0) + (l2_ptr.val if l2_ptr else 0) + carry
            keep = two_sum % 10
            carry = two_sum // 10

            new_ptr.next = ListNode(keep)
            new_ptr = new_ptr.next

            l1_ptr, l2_ptr = l1_ptr.next if l1_ptr else None, l2_ptr.next if l2_ptr else None
        if carry == 1:
            new_ptr.next = ListNode(carry)
        return new_head.next


