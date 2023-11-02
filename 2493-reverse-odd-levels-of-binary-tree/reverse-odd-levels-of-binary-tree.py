# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = []
        def bfs(root):
            q = deque([root])
            nextNodeVals = []
            depth = 0
            nextNodes = []
            while q:
                for x in range(len(q)):
                    node = q.pop()
                    if node:
                        if node.left:
                            nextNodes.append(node.left)
                        if node.right:
                            nextNodes.append(node.right)
                depth += 1
                if depth % 2:
                    for i in range(len(nextNodes)//2):
                        nextNodes[i].val, nextNodes[len(nextNodes)-1-i].val = nextNodes[len(nextNodes) -i - 1].val, nextNodes[i].val
                q, nextNodes = nextNodes, q
            return root
        return bfs(root)


