class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        dp = {}

        def dfs(i, buying, count):

            if i >= len(prices):
                return 0
            
            if count==2:
                return 0
            
            if (i,buying, count) in dp:
                return dp[(i,buying, count)]
            
            hold = dfs(i+1, buying = buying, count=count)
            
            if buying:
                buy = dfs(i+1, not buying, count) - prices[i]
                dp[(i,buying, count)] = max(buy, hold)
            else:
                sell = dfs(i+1, not buying, count+1) + prices[i]
                dp[(i,buying, count)] = max(sell, hold)
            
            print(f"{i} : {dp[(i, buying, count)]}")
            return dp[(i, buying, count)]

        return dfs(0, True, 0)
        

solution = Solution()
print(solution.maxProfit([3,3,5,0,0,3,1,4]))



# ------------------------OPTIMAL SOLUTION------------------------

# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         if not prices:
#             return 0

#         # Inițializăm variabilele pentru cele două tranzacții permise
#         buy1, sell1 = float('-inf'), 0
#         buy2, sell2 = float('-inf'), 0

#         for price in prices:
#             buy1 = max(buy1, -price)      # Prima achiziție (minim preț)
#             sell1 = max(sell1, buy1 + price)  # Prima vânzare (maxim profit după prima achiziție)
#             buy2 = max(buy2, sell1 - price)  # A doua achiziție (maxim profit după prima tranzacție)
#             sell2 = max(sell2, buy2 + price)  # A doua vânzare (maxim profit după a doua tranzacție)

#         return sell2  # Profit maxim după două tranzacții

# # Test
# solution = Solution()
# print(solution.maxProfit([3,3,5,0,0,3,1,4]))  # Output: 6
