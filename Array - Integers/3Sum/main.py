# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         res = []
#         dictionary = {}

#         for i,num in enumerate(nums):
#             dictionary[num] = i

#         for i in range(len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 summ = nums[i] + nums[j]
#                 complement = 0-summ
#                 if complement in nums and dictionary[complement] !=i and dictionary[complement]!=j:
#                     listed_sort = sorted([nums[i],nums[j],complement])
#                     # print(listed_sort)
#                     if listed_sort not in res:
#                         res.append(listed_sort)
        
#         return res

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, n-1

            while left < right:
                summ = nums[i] + nums[left] + nums[right]
                
                if summ == 0:
                    res.append([nums[i],nums[left],nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif summ < 0: 
                    left+=1
                else:
                    right-=1
        return res



solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))