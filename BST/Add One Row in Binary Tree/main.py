from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def _init_(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :type depth: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return val

        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        

        queue = deque([root])
        level_count = 1

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                element = queue.popleft()
                level.append(element)
                
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)

            level_count += 1

            if level_count == depth:
                for element in level:
                    left_child = TreeNode(val)
                    right_child = TreeNode(val)
                    left_child.left = element.left
                    right_child.right = element.right
                    
                    element.left = left_child
                    element.right = right_child

        return root