# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            leftTree = dfs(root.left)
            rightTree = dfs(root.right)
            leftMax = max(leftTree, 0)
            rightMax = max(rightTree, 0)

            res[0] = max(res[0], root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res 