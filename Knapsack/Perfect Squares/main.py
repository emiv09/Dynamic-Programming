from collections import deque

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        queue = deque([(n,0)])
        visited = set()

        while queue:
            num, level = queue.popleft()
            
            if num == 0:
                return level
            
            for i in range(1,int(n**0.5) +1):
                next_num = num - i*i
                if next_num not in visited:
                    visited.add(next_num)
                    queue.append((next_num, level+1))


solution = Solution()
print(solution.numSquares(4))

            
