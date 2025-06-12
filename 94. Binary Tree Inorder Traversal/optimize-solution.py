# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def traveseTree(node):
            if node:
                traveseTree(node.left)
                output.append(node.val)
                traveseTree(node.right)
        traveseTree(root)
        return output
