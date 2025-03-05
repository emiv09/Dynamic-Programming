class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        closest_sum = float('inf')

        for i in range(n-2):
            left = i+1
            right = n-1

            while left<right:
                summ = nums[i] + nums[left] + nums[right]
                if summ == target:
                    return summ
                
                if abs(target-summ) < abs(target-closest_sum):
                    closest_sum = summ
                
                if summ < target:
                    left += 1
                else: 
                    right-=1
        
        return closest_sum
    


solution = Solution()
print(solution.threeSumClosest([-1,2,1,-4], 1))