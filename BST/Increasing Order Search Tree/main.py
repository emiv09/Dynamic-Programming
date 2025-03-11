# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        def dfs(node, tail):
            if not node:
                return tail 
            
            new_root = dfs(node.left, node) 
            node.left = None  
            node.right = dfs(node.right, tail)  
            
            return new_root 

        return dfs(root, None)





root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(7)

solution = Solution()

print(solution.increasingBST(root))