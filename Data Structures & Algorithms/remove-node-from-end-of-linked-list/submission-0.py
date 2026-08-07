# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head

        prev = None
        left = dummy
        right = dummy
        for i in range(n):
            right = right.next
        
        while right:
            prev = left
            left = left.next
            right = right.next
        
        # now right is None and left is on the node we want to remove
        prev.next = left.next
        return dummy.next
        