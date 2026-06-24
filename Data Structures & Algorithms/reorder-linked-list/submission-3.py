# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. find middle node
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. reverse second half
        curr = slow.next
        prev = slow.next = None # slow.next = None prevents cycle
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # 3. merge the two halves
        first, second = head, prev
        while first.next and second:
            first_added, second_added = first.next, second.next
            first.next = second
            second.next = first_added
            first, second = first_added, second_added
        

        