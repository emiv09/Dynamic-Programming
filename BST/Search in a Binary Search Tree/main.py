# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        def dfs(node):
            if not node:
                return 
            
            if node.val == val: 
                return node
            
            elif node.val < val:
                return dfs(node.right)

            return dfs(node.left)
            


        return dfs(root)



root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

solution = Solution()

print(solution.searchBST(root, 2))