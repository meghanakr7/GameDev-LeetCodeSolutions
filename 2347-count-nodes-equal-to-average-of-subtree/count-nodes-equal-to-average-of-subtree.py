# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        d = defaultdict()
        c = 0
        res = []
        res1 = []
        allNodes = []

        def dfs(root):
            left = 0
            right = 0
            if root is None:
                return 0
            
            d[root.val] = root.val
            if root.left is None and root.right is None:
                d[root.val] = root.val
            if root.left:
                d[root.val] = d[root.val] + dfs(root.left)
            if root.right:
                d[root.val] = d[root.val] + dfs(root.right)
            res.append(d[root.val])
            allNodes.append(1 + left +right)
            return d[root.val]
        countNodes = []
        keys = []
        def dfscount(root):
            v = 0
            count = 1
            left = 0
            right = 0
            v = 1
            if root is None:
                return 0
                
            if root.left:
                left = dfscount(root.left)
                v = 1 + left
            if root.right:
                right = dfscount(root.right)
                v = v + right
            keys.append(root.val)
            countNodes.append(v)
            return v
        dfs(root)
        print("d is ",d)
        print("res is ",res)
        dfscount(root)
        print("CountNodes are ",countNodes)
        count = 0
        print("keys are ",keys)
        
        for i, val in enumerate(res):
            if res[i] // countNodes[i] == keys[i]:
                count += 1
            else:
                print("v ",res[i],countNodes[i],keys[i])
        return count