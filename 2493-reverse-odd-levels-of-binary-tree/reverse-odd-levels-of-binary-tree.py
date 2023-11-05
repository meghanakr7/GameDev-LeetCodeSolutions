# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nextNodes = []
        def bfs(root):
            q = deque([root])
            depth = 0
            while q:
                nextNodes = deque([])
                for x in range(len(q)):
                    node = q.popleft()
                    if node:
                        if node.left:
                            nextNodes.append(node.left)
                        if node.right:
                            nextNodes.append(node.right)
                    # print("before nextNodes ", nextNodes)   
                depth += 1
                # print("\ndepth is ",depth)
                if depth%2:
                    # print("\nentered\n")
                    for i in range(len(nextNodes)//2):
                        nextNodes[i].val, nextNodes[len(nextNodes)-i-1].val = nextNodes[len(nextNodes)-i-1].val, nextNodes[i].val
                # print("after nextNodes are ",nextNodes)
                q, nextNodes = nextNodes, q
            # print("root is ",root)
            return root
        return bfs(root)
                    


        