# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # find mid
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse starting from slow
        second = slow.next
        slow.next = None
        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge
        first = head
        second = prev

        while second:
            # Save next pointers
            tmp1, tmp2 = first.next, second.next
            
            # Weave them together
            first.next = second
            second.next = tmp1
            
            # Shift forward
            first = tmp1
            second = tmp2
