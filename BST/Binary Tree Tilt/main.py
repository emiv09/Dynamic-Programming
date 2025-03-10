# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def __init__(self):
        self.tilt = 0

    def findTilt(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node):
            if not node:
                return 0
            
            left_subtree = dfs(node.left)
            right_subtree = dfs(node.right)
            
            self.tilt += abs(left_subtree - right_subtree)

            return left_subtree + right_subtree + node.val
        
        dfs(root)
        return self.tilt

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

solution = Solution()

print(solution.findTilt(root))