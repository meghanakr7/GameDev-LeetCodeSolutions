# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        finalRes = []
        def dfs(node, res):
            if node is None:
                return
            res.append(node.val)
            if node.left is None and node.right is None:
                if sum(res) == targetSum:
                    finalRes.append(res[:])
            if node:
                dfs(node.left, res)
                dfs(node.right, res)
                if res:
                    res.pop()
        dfs(root, [])
        return finalRes

        