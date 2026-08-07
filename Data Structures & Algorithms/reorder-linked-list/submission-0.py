# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # head points to n-1
        # n-1 points to og head.next (1)
        # 1 points to n-2

        queue = deque()

        # if head is None
        curr = head.next
        while curr:
            queue.append(curr)
            curr = curr.next
        
        curr = head
        back = True
        while len(queue) > 0:
            if back:
                temp = queue.pop()
            else:
                temp = queue.popleft()
            
            back = not back

            curr.next = temp
            curr = curr.next
        
        # this is what i forget. assign last node to point to None
        curr.next = None
