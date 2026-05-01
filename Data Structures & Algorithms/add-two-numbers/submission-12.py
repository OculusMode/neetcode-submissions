# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        solN = None
        prev_ = 0
        temp_sol = None
        while l1 and l2:
            next_val = l1.val + l2.val + prev_
            next_, curr = divmod(next_val, 10)
            prev_ = next_
            node = ListNode(curr)
            if not temp_sol:
                solN = node
                temp_sol = node
            else:
                temp_sol.next = node
                temp_sol = temp_sol.next
            l1 = l1.next
            l2 = l2.next
        if l1 or l2:
            l = l1 if l1 else l2
            while l:
                next_val = l.val + prev_
                next_, curr = divmod(next_val, 10)
                prev_ = next_
                node = ListNode(curr)
                temp_sol.next = node
                temp_sol = temp_sol.next
                l = l.next
        if prev_ != 0:
            node = ListNode(prev_)
            temp_sol.next = node
        return solN