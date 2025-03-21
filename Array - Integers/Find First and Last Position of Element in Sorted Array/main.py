class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        def findBound(isFirst):
            left = 0
            right = len(nums) - 1
            bound = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    bound = mid

                    if isFirst:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return bound
        
        leftBound = findBound(True)
        rightBound = findBound(False)

        return [leftBound, rightBound]

          


