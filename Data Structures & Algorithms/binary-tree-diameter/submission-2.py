# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height_and_diam(self, root, max_diam):
        if not root:
            return 0, 0
        height_left, diam_max_left = self.height_and_diam(root.left, max_diam)
        height_right, diam_max_right = self.height_and_diam(root.right, max_diam)
        height = 1 + max(height_left, height_right)
        diam = max(height_left + height_right, diam_max_left, diam_max_right)
        return height, diam

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.height_and_diam(root, 0)[1]