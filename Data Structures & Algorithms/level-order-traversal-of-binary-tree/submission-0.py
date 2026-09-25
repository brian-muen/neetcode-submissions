class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
    
        queue = deque([(root, 0)])

        curr_level = 0
        partial = []
        res = []

        if not root:
            return []
        else:
            res.append([root.val])


        while queue:
            node, level = queue.popleft()

            if level != curr_level:
                res.append(partial.copy())
                partial = []
                curr_level += 1

            if node.left:
                partial.append(node.left.val)
                queue.append((node.left, level + 1))

            if node.right:
                partial.append(node.right.val)
                queue.append((node.right, level + 1))

        return res