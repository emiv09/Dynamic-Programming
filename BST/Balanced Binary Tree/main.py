# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def getHeight(node):
            if not node:
                return -1 
            
            return 1 + max(getHeight(node.left), getHeight(node.right))
        
        def dfs(node):
            if not node:
                return True
            
            left = getHeight(dfs(node.left))
            right = getHeight(dfs(node.right))

            if abs(left-right) < 2:
                root.val = 
            
            return root.val


        return dfs(root)


root = TreeNode(3)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(4)
root.left.right = TreeNode(3)
root.right = TreeNode(2)

solution = Solution()
print(solution.isBalanced(root))