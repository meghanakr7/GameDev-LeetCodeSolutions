# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        def bfs(root):
            q = deque([root])
            nextValues = []
            nextNodes = []
            depth = 0
            if root.val % 2 == 0:
                return False
            while q:
                nextNodes = deque([])
                nextValues = []
               
                for x in range(len(q)):
                    node = q.popleft()
                    if node:
                        if node.left:
                            nextNodes.append(node.left)
                            nextValues.append(node.left.val)
                        if node.right:
                            nextNodes.append(node.right)
                            nextValues.append(node.right.val)
                depth += 1
                # print("nextValues ",nextValues, set(nextValues), sorted(set(nextValues)), depth)
                for i in range(len(nextValues)):
                    if nextValues[i]%2 == depth % 2:
                        print("nextValues and depth is ",nextValues[i], depth)
                        return False
                if depth%2 == 1 and sorted(set(nextValues), reverse = True) != nextValues:
                    print("nextValues, ",nextValues, sorted(set(nextValues)),sorted(set(nextValues), reverse = True) )
                    print("in line 31")
                    return False
                if depth%2 == 0 and sorted(set(nextValues)) != nextValues:
                    print("sorted ",sorted(set(nextValues)), nextValues, sorted(nextValues))
                    print("in line 34")
                    return False
                q, nextNodes = nextNodes, q
            return True
        return bfs(root)

            