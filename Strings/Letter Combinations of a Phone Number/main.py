class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dictionary = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        
        def backtrack(i, currString):
            if len(currString) == len(digits):
                res.append(currString)
                return
            
            for c in dictionary[digits[i]]:
                backtrack(i+1, currString+c)

        if digits:
            backtrack(0,"")
        return res



solution = Solution()
print(solution.letterCombinations("23"))