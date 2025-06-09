# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def travese(node):
            if node:
                output.append(node.val)
                travese(node.left)
                travese(node.right)
        
        travese(root)
        return output