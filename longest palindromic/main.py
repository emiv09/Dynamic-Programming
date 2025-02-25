class Solution(object):
    
    def longestPalindrome(self, s):
       
        start = 0
        endi = len(s)-1

        substring = ''
        while start < len(s):
            while start < endi:
                reversed_s = s[start:endi:-1]
                if s[start:endi] == reversed_s:
                    if endi-start+1 > len(substring):
                        substring = s[start:endi]
                
                endi -= 1
            start += 1

        return substring


       
        


solution = Solution()

print(solution.longestPalindrome("abad"))
        
