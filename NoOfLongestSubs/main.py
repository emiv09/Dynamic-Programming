class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        length = [1] * n
        count = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j]+1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    
                    elif length[j] + 1 == length[i]:
                        count[i] = count[j] + 1
        
        return sum(count[i] for i in range(n) if length[i]==max(length))
    


