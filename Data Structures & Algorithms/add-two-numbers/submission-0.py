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
            if l1_ptr and l2_ptr:
                two_sum = l1_ptr.val + l2_ptr.val
            elif l1_ptr:
                two_sum = l1_ptr.val 
            else:
                two_sum = l2_ptr.val
            two_sum += carry
            keep = two_sum % 10
            carry = two_sum // 10

            new_ptr.next = ListNode(keep)
            new_ptr = new_ptr.next

            if l1_ptr:
                l1_ptr = l1_ptr.next
            if l2_ptr:
                l2_ptr = l2_ptr.next
        if carry == 1:
            new_ptr.next = ListNode(carry)
        return new_head.next


