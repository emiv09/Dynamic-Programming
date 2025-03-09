from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        queue = deque([root])
        level = 0 
        while queue:
            level_size = len(queue)
            maxi = float('inf')
            mini = float('-inf')

            for _ in range(level_size):
                node = queue.popleft()
                element = node.val
                if level % 2 == 0:
                    if element %2 == 0 or element < mini:
                        return False
                    mini = element
                else:
                    if element %2 !=0 or element > maxi:
                        return False
                    maxi = element
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level += 1
       
        return True
    

root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.right = TreeNode(2)
root.right.left = TreeNode(7)

solution = Solution()
print(solution.isEvenOddTree(root)) 