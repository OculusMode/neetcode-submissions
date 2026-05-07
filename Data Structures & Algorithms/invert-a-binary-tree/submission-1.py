# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        head = root
        left = head.left
        head.left = head.right
        head.right = left
        head.left = self.invertTree(head.left)
        head.right = self.invertTree(head.right)
        return head