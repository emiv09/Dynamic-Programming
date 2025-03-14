from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        if not root:
            return []

        res = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                element = queue.popleft()
                
                if element:
                    res.append(element.val)
                    queue.append(element.left)
                    queue.append(element.right)
                
                else:
                    res.append(None)
                

                
            for i in range(len(res)-1,-1,-1):
                if res[i] == None:
                    res.pop()
                else: 
                    break
        return res
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)


ser = Codec()

print(ser.serialize(root))



                    
                


                

    
