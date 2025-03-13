from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        if not root:
            return 0
        
        
        res = 1
        queue = deque([(root,1)])
        
        while queue:
            level_size = len(queue)
            _, start = queue[0]
            _, end = queue[-1]

            res = max(res, end-start+1)

            for _ in range(level_size):
                element, index = queue.popleft()
                if element.left:
                    queue.append(element.left, 2*index)
                if element.right:
                    queue.append(element.right, 2*index+1)
            

        return res


            


root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)

solution = Solution()

print(solution.widthOfBinaryTree(root))