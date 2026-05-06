# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        curr_head = None
        while True:
            val = 1001
            max_node = None
            max_idx = 1001
            for idx, l in enumerate(lists):
                if not l:
                    continue
                if l.val < val:
                    max_node = l
                    max_idx = idx
                    val = l.val
            if not head:
                head = max_node
                curr_head = max_node
            else:
                curr_head.next = max_node
                curr_head = curr_head.next
            if max_node:
                print(max_node.val)
                lists[max_idx] = lists[max_idx].next
            else:
                print("returning")
                return head
