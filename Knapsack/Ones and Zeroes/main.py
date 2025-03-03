class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        
        dp = {}

        def dfs(i, m, n):
            if i==len(strs):
                return 0
            if (i,m,n) in dp:
                return dp[(i,m,n)]
            
            m_count = strs[i].count("0")
            n_count = strs[i].count("1")

            if m_count <= m and n_count <= n:
                dp[((i,m,n))] = max(1+ dfs(i+1, m-m_count, n-n_count), dfs(i+1,m,n))
            else:
                dp[((i,m,n))] = dfs(i+1,m,n)
            
            return dp[((i,m,n))]
        
        return dfs(0,m,n)

solution = Solution()
print(solution.findMaxForm(["10","0001","111001","1","0"],5,3))