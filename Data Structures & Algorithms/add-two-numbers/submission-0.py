# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l3 = ListNode()
        l3_head = l3

        overflow = 0

        # reverse the two lists
        # curr = l1
        # prev = None
        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp

        # curr = l2
        # prev = None
        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp

        # add them together
        
        overflow = False

        curr_l1 = l1
        curr_l2 = l2
        while curr_l1 or curr_l2 or overflow:
            l1_val = curr_l1.val if curr_l1 else 0
            l2_val = curr_l2.val if curr_l2 else 0

            val = l1_val + l2_val + overflow

            overflow = True if val >= 10 else False

            val = val - 10 if overflow else val

            temp = ListNode(val)
            l3.next = temp
            l3 = l3.next

            curr_l1 = curr_l1.next if curr_l1 else None
            curr_l2 = curr_l2.next if curr_l2 else None
        
        return l3_head.next