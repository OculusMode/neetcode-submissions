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
        if not head:
            return
        node_to_node = {}
        curr_head = head
        nhead = None
        idx = 0
        while curr_head:
            curr = Node(curr_head.val)
            node_to_node[curr_head] = curr
            if nhead:
                nhead.next = curr
                nhead = nhead.next
            else:
                nhead = curr
                nhead_first = curr
            curr_head = curr_head.next
        curr_head = head
        nhead = nhead_first
        # print(node_to_node)
        while nhead:
            if curr_head.random:
                nhead.random = node_to_node[curr_head.random]
            # else:
            #     nhead.random = None
            curr_head = curr_head.next
            nhead = nhead.next
        return nhead_first

                