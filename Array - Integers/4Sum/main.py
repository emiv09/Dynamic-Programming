class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        n = len(nums)
        start = 0
        while start < n-3:
            if start >= 1 and  nums[start] == nums[start-1]:
                start += 1
                continue

            end = n-1
            
            while end > start+2: 
                if end < n-1 and nums[end] == nums[end+1]:
                    end -= 1
                    continue
                
                left = start+1
                right = end-1

                while left < right:
                    summ = nums[start]+nums[end]+nums[left]+nums[right]
                    if summ == target:
                        res.append([nums[start],nums[left],nums[right],nums[end]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        
                        left += 1
                        right -= 1
                    elif summ<target:
                        left += 1
                    elif summ>target:
                        right -= 1
                    
                
                end-=1
            start+=1

        return res
    

solution = Solution()
print(solution.fourSum([2,2,2,2,2], 8))
print(solution.fourSum([-2,-1,0,0,1,2], 0))



