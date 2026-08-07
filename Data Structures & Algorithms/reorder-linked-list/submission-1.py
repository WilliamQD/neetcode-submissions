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

        ### brute force
        # queue = deque()

        # # if head is None
        # curr = head.next
        # while curr:
        #     queue.append(curr)
        #     curr = curr.next
        
        # curr = head
        # back = True
        # while len(queue) > 0:
        #     if back:
        #         temp = queue.pop()
        #     else:
        #         temp = queue.popleft()
            
        #     back = not back

        #     curr.next = temp
        #     curr = curr.next
        
        # # this is what i forget. assign last node to point to None
        # curr.next = None


        ### reverse and merge (optimal)
        slow = head
        fast = head

        # find mid
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # mid = slow

        # reverse starting from mid

        prev = None

        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # start merging
        left = head

        back = True
        while left and prev:
            if back:
                next_node = left.next
                left.next = prev
                
                back = not back
                left = next_node
            else:
                next_node = prev.next
                prev.next = left

                back = not back
                prev = next_node
        
        if back:
            left.next = None
        else:
            prev.next = None

        

