class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        dp = {}
        max_length = 0

        for num in arr:
            dp[num] = dp.get(num - difference, 0) + 1
            max_length = max(max_length, dp[num])    

        return max_length

solution = Solution()

print(solution.longestSubsequence([1,2,3,4],1))