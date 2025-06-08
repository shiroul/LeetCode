# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        if not root:
            return output

        def traveseTree(node):
            if not node:
                return
            
            traveseTree(node.left)

            output.append(node.val)

            traveseTree(node.right)
        
        traveseTree(root.left)
        output.append(root.val)
        traveseTree(root.right)

        return output