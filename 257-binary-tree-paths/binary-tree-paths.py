# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def dfs(node, path):
            if not node:
                return

            # If this is a leaf node
            if not node.left and not node.right:
                res.append(path + str(node.val))
            else:
                # Continue path with current node
                path += str(node.val) + "->"
                dfs(node.left, path)
                dfs(node.right, path)

        dfs(root, "")
        return res
        