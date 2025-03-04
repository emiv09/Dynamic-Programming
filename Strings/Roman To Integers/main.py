class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        num = 0

        dictionary = {"I": 1, "V": 5, "X":10, "L":50,
                      "C": 100, "D":500, "M":1000}

        i = 0

        while i<len(s)-1:
            ch = s[i]
            next_ch = s[i+1]
            if ch == "I" and (next_ch == "V" or next_ch=="X"):
                num += dictionary[next_ch] - dictionary[ch]
                i += 2
            elif ch == "X" and (next_ch == "L" or next_ch=="C"):
                num += dictionary[next_ch] - dictionary[ch]
                i += 2
            elif ch == "C" and (next_ch == "D" or next_ch=="M"):
                num += dictionary[next_ch] - dictionary[ch]
                i += 2
            else:
                num += dictionary[ch]
                i+=1
        if i == len(s)-1:
            num += dictionary[s[len(s)-1]]
        return num
    

solution = Solution()
print(solution.romanToInt("III"))