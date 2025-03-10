from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        if root is None:
            return True

        queue = deque([root.left, root.right])
        
        while queue:

            element1 = queue.popleft()
            element2 = queue.popleft()

            if not element1 and not element2:
                continue

            if not element1 or not element2 or element1.val != element2.val:
                return False
            
            queue.append(element1.left)
            queue.append(element2.right)
            queue.append(element1.right)
            queue.append(element2.left)
        
        return True

            
        
        

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.left = TreeNode(4)

# root = TreeNode(1)
# root.left = TreeNode(2)
# # root.left.left = TreeNode(3)
# root.left.right = TreeNode(3)
# root.right = TreeNode(2)
# root.right.right = TreeNode(3)
# # root.right.left = TreeNode(4)

solution = Solution()
print(solution.isSymmetric(root))