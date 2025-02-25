class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        
        envelopes.sort(key = lambda x : (x[0], x[1]))
        count = 0
        max_width = 0
        max_height = 0 

        for width, height in envelopes:
            if width > max_width and height > max_height:
                count += 1
                max_width = width
                max_height = height

        return count

solution = Solution()
print(solution.maxEnvelopes([[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]))