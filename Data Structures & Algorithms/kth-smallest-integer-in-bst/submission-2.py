# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        counter = 0

        def inorder(node):
            nonlocal counter

            if node is None:
                return None

            res = inorder(node.left)
            if res is not None:
                return res
            
            counter += 1
            if counter == k:
                return node.val
            
            return inorder(node.right)
        
        return inorder(root)
