class Solution(object):
    def longestArithSeqLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        dp = [{} for _ in range(n)]

        for i in range(1,n):
            for j in range(i):
                dp[i][nums[i]-nums[j]] = dp[j].get(nums[i]-nums[j],1) + 1

        max_length = 2
        for i in range(1,n):
            max_length = max(max(dp[i].values()), max_length)
        
        return max_length

solution = Solution()
print(solution.longestArithSeqLength([9,4,7,2,10]))