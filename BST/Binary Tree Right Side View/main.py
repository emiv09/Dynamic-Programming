from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        
        res = []
        queue = deque([root])

        while queue:
            count = 0

            for _ in range(len(queue)):
                element = queue.popleft()
                if count == 0:
                    res.append(element.val)
                    count +=1
                
                if element.right:
                    queue.append(element.right)
                if element.left:
                    queue.append(element.left)
        
        return res



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.left.right = TreeNode(5)

solution = Solution()

print(solution.rightSideView(root))