# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def sameTree(s,t):
            if not s and not t:
                return True
            if s and t and s.val == t.val:
                return sameTree(s.left, t.left) and sameTree(s.right, t.right)
            
            return False
        
        if not subRoot: return True
        if not root: return False

        if sameTree(root,subRoot):
            return True
         
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
