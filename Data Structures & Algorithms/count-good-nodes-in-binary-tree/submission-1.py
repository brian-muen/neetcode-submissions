# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0
        queue = deque([(root, float("-inf"))])

        while queue:
            node, path_max = queue.popleft()

            if node.val >= path_max:
                res += 1

            if node.left:
                queue.append((node.left, max(path_max, node.val)))
            if node.right:
                queue.append((node.right, max(path_max, node.val)))

            
        return res






        