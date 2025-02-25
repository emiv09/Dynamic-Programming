class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """

        m = len(s1)
        n = len(s2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]        
        
        for i in range(1,m+1):
            dp[i][0] = ord(s1[i-1]) + dp[i-1][0]
        
        for j in range(1,n+1):
            dp[0][j] = ord(s2[j-1]) + dp[0][j-1]


        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    if dp[i-1][j] <= dp[i][j-1]:
                        dp[i][j] = ord(s1[i-1]) + dp[i-1][j]
                    else: 
                        dp[i][j] = ord(s2[j-1]) + dp[i][j-1]
        return dp[m][n]



solution = Solution()
print(solution.minimumDeleteSum("sea","eat"))
        