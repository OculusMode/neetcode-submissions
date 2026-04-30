# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        tail = head
        prev = None
        while True:
            # save next
            next_ = tail.next
            # change ref
            tail.next = prev
            # update prev for next run
            prev = tail
            if not next_:
                break
            # update tail
            tail = next_
        return tail