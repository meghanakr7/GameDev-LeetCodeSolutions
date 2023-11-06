# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        finalRes = []
        def bfs(root):
            q = deque([root])
            if root:
                res = [root.val]
                finalRes.append(res)
            while q:
                nextNodes = deque()
                res = []
                for x in range(len(q)):
                    node = q.popleft()
                    if node:
                        if node.left:
                            res.append(node.left.val)
                            nextNodes.append(node.left)
                        if node.right:
                            nextNodes.append(node.right)
                            res.append(node.right.val)
                q = nextNodes
                if len(res):
                    finalRes.append(res)
        bfs(root)
        return finalRes