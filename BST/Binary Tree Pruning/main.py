# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        
        
        def dfs(node):
            if not node:
                return None
            
            left = dfs(node.left)
            right = dfs(node.right)

            if node.val != 1 and not left and not right:
                return None 
            
            return node
            
        
        return(dfs(root))
        




root = TreeNode(1)
root.right = TreeNode(0)
root.right.right = TreeNode(1)
root.right.left = TreeNode(0)

solution = Solution()
print(solution.pruneTree(root))