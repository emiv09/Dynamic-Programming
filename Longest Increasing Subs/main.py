class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        dp = [1] * n

        total_count = 0

        for i in range(1,n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
            
        
        for x in range(n):
            if dp[x] == max(dp)-1:
                total_count+=1
        
        

        return total_count


solution = Solution()
print(solution.lengthOfLIS([1,3,5,4,7]))