# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1
        h2 = list2
        if not h1:
            return list2
        if not h2:
            return list1
        if h1.val < h2.val:
            res = h1
            h1 = h1.next
        else:
            res = h2
            h2 = h2.next
        main_res = res
        while h1 and h2:
            if h1.val < h2.val:
                res.next = h1
                h1 = h1.next
            else:
                res.next = h2
                h2 = h2.next
            res = res.next
        while h1:
            res.next = h1
            h1 = h1.next
            res = res.next
        while h2:
            res.next = h2
            h2 = h2.next
            res = res.next
        return main_res