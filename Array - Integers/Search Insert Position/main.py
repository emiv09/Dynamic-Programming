class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0 
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid+1
            else:
                right = mid
        
        return right
    


solution = Solution()
print(solution.searchInsert([1,3,5,6],5))
print(solution.searchInsert([1,3,5,6],2))
print(solution.searchInsert([1,3,5,6],7))

