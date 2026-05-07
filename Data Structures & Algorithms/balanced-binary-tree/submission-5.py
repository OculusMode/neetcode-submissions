# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height_and_balance(self, root):
        if not root:
            return 0, True
        height_left, balance_left = self.height_and_balance(root.left)
        height_right, balance_right = self.height_and_balance(root.right)
        return 1+max(height_left,height_right), balance_left and balance_right and (height_left - height_right) in [1, -1, 0]

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height_and_balance(root)[1]