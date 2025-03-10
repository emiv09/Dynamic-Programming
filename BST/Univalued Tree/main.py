# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
    
        def dfs(node, val):
            if not node:
                return

            if node.val != val:
                return False

            left_tree = dfs(node.left, val)
            right_tree = dfs(node.right, val)
            
            if left_tree==False or right_tree==False:
                return False

            return True
        
        return dfs(root, root.val)
        
       


root = TreeNode(2)
root.left = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(2)
root.right = TreeNode(2)

solution = Solution()
print(solution.isUnivalTree(root))