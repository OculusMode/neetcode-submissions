# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast_pointer = head
        slow_pointer = head
        while True:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
            if not slow_pointer or not fast_pointer or not fast_pointer.next:
                return False
            fast_pointer = fast_pointer.next
            if not fast_pointer:
                return False
            if fast_pointer.val == slow_pointer .val:
                return True
            
