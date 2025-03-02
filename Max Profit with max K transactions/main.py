class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        
        dp = {}

        def dfs(i, buying, count):

            if i>=len(prices):
                return 0
            
            if count==k:
                return 0
            
            if (i,buying,count) in dp:
                return dp[(i, buying, count)]
            
            hold = dfs(i+1, buying=buying, count=count)

            if buying:
                buy = dfs(i+1, not buying, count) - prices[i]
                dp[(i, buying, count)] = max(buy, hold)
            
            else: 
                sell = dfs(i+1, not buying, count+1) + prices[i]
                dp[(i, buying, count)] = max(sell, hold)
            
            return dp[(i, buying, count)]
        
        return dfs(0, True, 0)
    

solution = Solution()
print(solution.maxProfit(2,[3,2,6,5,0,3]))



# ----------------------------OPTIMAL SOLUTION----------------------------

# class Solution(object):
#     def maxProfit(self, k, prices):
#         """
#         :type k: int
#         :type prices: List[int]
#         :rtype: int
#         """
#         if not prices or k == 0:
#             return 0

#         n = len(prices)

#         # Dacă k >= n/2, problema devine Best Time to Buy and Sell Stock II (tranzacții nelimitate)
#         if k >= n // 2:
#             return sum(max(prices[i + 1] - prices[i], 0) for i in range(n - 1))

#         # DP cu O(nk) timp și O(k) spațiu
#         prev = [0] * (n)  # Profit pentru t-1 tranzacții
#         curr = [0] * (n)  # Profit pentru t tranzacții

#         for t in range(1, k + 1):
#             maxDiff = -prices[0]  # max(dp[t-1][j] - prices[j])
#             for i in range(1, n):
#                 curr[i] = max(curr[i - 1], prices[i] + maxDiff)
#                 maxDiff = max(maxDiff, prev[i] - prices[i])  # Actualizăm maxDiff
#             prev, curr = curr, prev  # Swap array-urile

#         return prev[-1]  # Profit maxim

