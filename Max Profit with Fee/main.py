class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp={}

        def dfs(i, buying):
            if i>=len(prices):
                return 0
            
            if (i,buying) in dp:
                return dp[(i,buying)]
            
            hold = dfs(i+1, buying=buying) 

            if buying: 
                buy = dfs(i+1, not buying) - prices[i]
                dp[(i,buying)] = max(buy, hold)
            else:
                sell = dfs(i+1, not buying) + prices[i] - 2 
                dp[(i,buying)] = max(sell, hold)

            return dp[(i, buying)]

        return dfs(0,True)

    

solution = Solution()
print(solution.maxProfit([1,3,2,8,4,9],2))