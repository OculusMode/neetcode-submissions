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
            next_ = tail.next
            tail.next = prev
            print(tail.val)
            if tail.next:
                print("next", tail.next.val)
            prev = tail
            if not next_:
                break
            tail = next_
        return tail