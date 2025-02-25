class Solution(object):
    def wordBreak(self, s, wordDict):
        i=0
        while i <= len(s):
            if s[0:i] in wordDict:
                s = s[i:]
                i=0
            else:
                i += 1
        
        if s=="":
            return True
        return False
    


solution = Solution()
print(solution.wordBreak("aaaaaaa",["aaaa","aaa"]))