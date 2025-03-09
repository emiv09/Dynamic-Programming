# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def dfs(node, path):
            if not node:
                return 0

            path += str(node.val) 

            if not node.left and not node.right:
                return int(path)
        
            return dfs(node.left, path) + dfs(node.right, path)

        return dfs(root, "")
    

root = TreeNode(4)
root.left = TreeNode(9)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)
root.right = TreeNode(0)

solution = Solution()
print(solution.sumNumbers(root))

            
