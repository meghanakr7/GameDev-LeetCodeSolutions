# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d = defaultdict()
        q = deque([root])
        def bfs(node):
            while q:
                node = q.pop()
                if node.val not in d:
                    d[node.val] = 1
                else:
                    d[node.val] += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        bfs(root)
        sorted_items = sorted(d.items(),key = lambda x:x[1], reverse = True)
        largest_value_keys = [item[0] for item in sorted_items if item[1] == sorted_items[0][1]]
        d = sorted(d.values(), reverse = True)
        return largest_value_keys
                
            

        