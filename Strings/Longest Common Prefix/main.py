class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        sorted_strs = sorted(strs, key = len)

        longest = sorted_strs[0]

        for i in range(1,len(sorted_strs)):
            for j in range(len(longest)):
                if sorted_strs[i][j] != longest[j]:
                    longest = longest[0:j]
                    if longest == "":
                        return longest
                    break

        
        return longest
    

solution = Solution()
print(solution.longestCommonPrefix(["dog","racecar","car"]))