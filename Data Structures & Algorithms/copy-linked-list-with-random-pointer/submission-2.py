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
        # dummy = Node(x=0)
        
        # # random pointer points to the position of the node, not its value

        # node_map = {}

        # curr = head
        # prev = dummy

        # while curr:
        #     temp = Node(x=curr.val, next=None, random=None)

        #     prev.next = temp
        #     prev = temp

        #     node_map[curr] = temp
        #     curr = curr.next

        
        # curr_dum = dummy.next
        # curr = head

        # while curr_dum:
        #     if curr.random:
        #         curr_dum.random = node_map[curr.random]
        #     else:
        #         curr_dum.random = None

        #     curr_dum = curr_dum.next
        #     curr = curr.next
        
        # return dummy.next

        ### doing without a dummy
        node_map = {None:None}

        curr = head
        while curr:
            temp = Node(curr.val)
            node_map[curr] = temp
            curr = curr.next
        
        curr = head
        while curr:
            node_map[curr].random = node_map[curr.random]
            node_map[curr].next = node_map[curr.next]
            curr = curr.next

        return node_map[head]

        ### O(1) space

        curr = head
        while curr:
            copy = Node(curr.val, curr.next, random=None)
            curr.next = copy
            curr = copy.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        curr = head

        while curr:
            og_next = curr.next.next
            curr.next = og_next.next
            curr = og_next
        
        return head.next

