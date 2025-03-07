class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        res = []


        def backtrack(currentString, opened, closed):
            if opened == closed == n:
                res.append(currentString)
                return 
            
            if opened < n:
                backtrack(currentString + "(", opened+1, closed)
            
            if closed < opened:
                backtrack(currentString + ")", opened, closed+1)

        
        backtrack("",0,0)
        return res

            
        