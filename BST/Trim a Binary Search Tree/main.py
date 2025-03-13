# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: Optional[TreeNode]
        """

        def dfs(node):
            if not node:
                return None
            
            if node.val <= high and node.val >= low:
                node.left = dfs(node.left)
                node.right = dfs(node.right)
                return node
            
            if node.val > high:
                new_root = node.left
                return dfs(new_root)

            if node.val < low:
                new_root = node.right
                return dfs(new_root)
        
        return dfs(root)
                

root = TreeNode(3)
root.left = TreeNode(0)
root.right = TreeNode(4)
# root.left.left = TreeNode(5)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(1)

solution = Solution()

print(solution.trimBST(root,1,3))