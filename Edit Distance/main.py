class Solution(object):
    def minDistance(word1, word2) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Inițializăm cazurile de bază
        for i in range(m + 1):
            dp[i][0] = i  # Transformăm `word1[0:i]` în ""
        for j in range(n + 1):
            dp[0][j] = j  # Transformăm "" în `word2[0:j]`
        
        # Umplem tabela dp
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:  # Dacă sunt egale, nu facem nimic
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j],   # Ștergere
                                    dp[i][j - 1],   # Inserare
                                    dp[i - 1][j - 1])  # Înlocuire

        return dp[m][n]




solution = Solution()
solution.minDistance("horse","ros")

            



        