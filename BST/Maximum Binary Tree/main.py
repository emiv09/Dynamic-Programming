# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        
        def build_tree(arr):
            if not arr:
                return
            max_index = arr.index(max(arr))

            node = TreeNode(arr[max_index])
            
            prefix = arr[0:max_index]
            sufix = arr[max_index+1:]
            if prefix:
                node.left = build_tree(prefix)
            if sufix:
                node.right = build_tree(sufix)
            
            return node


        return build_tree(nums)


solution = Solution()
print(solution.constructMaximumBinaryTree([3,2,1,6,0,5]))