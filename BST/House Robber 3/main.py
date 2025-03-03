# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # [leftPair, rightPair]
        def dfs(root):
            if not root:
                return [0,0]
            
            leftPair = dfs(root.left)
            rightPair = dfs(root.right)

            withRoot = leftPair.val + rightPair.val
            withoutRoot = max(leftPair) + max(rightPair)

            return [withRoot, withoutRoot]
        
        return max(dfs(root))