# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(node1: TreeNode, node2: TreeNode) -> bool:
            if node1 is None and node2 is None:
                return True

            if node1 is None or node2 is None or node1.val != node2.val:
                return False

            return isMirror(node1.left,node2.right) and isMirror(node1.right, node2.left)


        return isMirror(root, root)

            