class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x : x[1])
        curr_end = float('-inf')
        


solution = Solution()
print(solution.findLongestChain([[1,2],[7,8],[4,5]]))