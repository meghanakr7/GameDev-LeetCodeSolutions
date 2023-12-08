# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(root):
            if root:
                res.append(str(root.val))
                if not root.left and not root.right:
                    return
                res.append('(')
                dfs(root.left)
                res.append(')')
                if root.right:
                    res.append('(')
                    dfs(root.right)
                    res.append(')')
        print('root' ,res)
        dfs(root)
        print('res is ',res)
        print('res str is ',"".join(res))
        return "".join(res)
        