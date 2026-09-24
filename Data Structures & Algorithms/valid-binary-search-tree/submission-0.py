# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        curr = float("-inf")
    
        def inorder(node):
            nonlocal curr 

            if node is None:
                return True

            if not inorder(node.left):
                return False

            if curr is not None and curr >= node.val:
                return False
            curr = node.val

            return inorder(node.right)

        

        return inorder(root)


            
        