# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: 
            return "N"

        string = []

        queue = deque([root])

        while queue:
            node = queue.popleft()

            if not node:
                string.append("N")
                continue
            
            string.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)


        string = ",".join(string)
        return string


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        if data == "N": return None

        values = data.split(",")

        root = TreeNode(int(values[0]))
        queue = deque([root])

        idx = 1

        while queue:
            node = queue.popleft()

            if values[idx] != "N":
                node.left = TreeNode(values[idx])
                queue.append(node.left)
            idx += 1

            if values[idx] != "N":
                node.right = TreeNode(values[idx])
                queue.append(node.right)
            idx += 1
            
            
        return root


            


