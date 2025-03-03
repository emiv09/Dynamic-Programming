class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dic = {}
        
        for i, num in enumerate(nums):
            complement = target-num 
            if complement in dic:
                return [dic[complement], i]
            dic[num] = i
        
        return []
    
        