# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def printTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[str]]
        """

        def getHeight(node):
            if not node:
                return -1

            return max(getHeight(node.left), getHeight(node.right)) + 1
        
        height = getHeight(root)
        m = height + 1
        n = (pow(2,m) - 1)
        matrix = [[""] * n for _ in range(m)]
        matrix[0][(n-1) // 2] = str(root.val)

        def build_matrix(node,r,c):
            if not node:
                return
            if node.left:
                matrix[r+1][c-pow(2,height-r-1)] = str(node.left.val)
                build_matrix(node.left,r+1,c-pow(2,height-r-1))
            if node.right:
                matrix[r+1][c+pow(2,height-r-1)] = str(node.right.val)             
                build_matrix(node.right,r+1,c+pow(2,height-r-1))            


        build_matrix(root, 0, (n-1) // 2)
        return matrix



root = TreeNode(1)
root.left = TreeNode(2)
# root.left.right = TreeNode(4)
# root.right = TreeNode(3)

solution = Solution()
print(solution.printTree(root))