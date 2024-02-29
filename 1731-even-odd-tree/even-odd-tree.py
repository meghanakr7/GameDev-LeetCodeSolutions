# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        d = defaultdict(list)
        def bfs(root,level):
            if root is None:
                return True
            print(root.val)
            d[level].append(root.val)
            if level% 2 == 0:
                if(root.val%2 == 0):
                    print('here in if ',root.val)
                    return False
            else:
                if(root.val%2 == 1):
                    print('here in right ',root.val)
                    return False
            
            return bfs(root.left, level + 1) and bfs(root.right, level + 1)
        if not bfs(root,0):
            print('here')
            return False
        print('d is ',d)
        for i in range(len(d)):
            if len(d[i]) != len(set(d[i])):
                return False
            temp = d[i]
            if i%2 == 0:
                if(sorted(temp) != d[i]):
                    return False
            else:
                if(sorted(temp,reverse = True) != d[i]):
                    return False
        return True