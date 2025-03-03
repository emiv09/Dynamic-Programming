class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_string = []
        cnt = 0

        for ch in s: 
            if ch == "(":
                cnt += 1
                new_string.append(ch)
            elif ch == ")" and cnt > 0:
                cnt -= 1
                new_string.append(ch)
            elif ch != ")":
                new_string.append(ch)
            
        res = []

        for ch in new_string[::-1]:
            if ch == "(" and cnt > 0:
                cnt -= 1
                continue
            res.append(ch)
        
        return "".join(res[::-1])

solution = Solution()
print(solution.minRemoveToMakeValid("(a(b(c)d)"))