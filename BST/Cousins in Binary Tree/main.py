from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """
        if not root:
            return False
        
        flag = False
        queue = deque([(root,None)])

        while queue:
            level = []
            level_size = len(queue)

            for _ in range(level_size):
                element, parent = queue.popleft()
                level.append((element,parent))
            
            parent1, parent2 = None, None

            for element, parent in level:
                if not element:
                    continue
                if element.val == x:
                    parent1 = parent
                elif element.val == y:
                    parent2 = parent
            
            if parent1 and parent2:
                return parent1 != parent2
            
            for element, parent in level:
                if element.left:
                    queue.append((element.left, element))
                if element.right:
                    queue.append((element.right, element))
                
            
        return False
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(5)
root.left.right = TreeNode(4)

solution = Solution()

print(solution.isCousins(root,4,3))