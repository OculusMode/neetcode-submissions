# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        tot = 0
        temp_head = head
        while temp_head:
            tot+=1
            temp_head = temp_head.next
        if tot == 1:
            return None
        nth = tot - n
        temp_head = head
        c = 1
        if nth == 0:
            return temp_head.next
        while c < nth:
            temp_head = temp_head.next
            c += 1
        if temp_head.next.next:
            temp_head.next = temp_head.next.next
        else:
            temp_head.next = None
        return head