# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(root, cur, res):
            if root is None:
                return
            cur.append(str(root.val))
            if root.left is None and root.right is None:
                res.append("->".join(cur))
            dfs(root.left, cur, res)
            dfs(root.right, cur, res)
            cur.pop()
        res = []
        dfs(root, [], res)
        return res