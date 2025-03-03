# from collections import deque

# class Solution(object):
#     def combinationSum4(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         queue = deque([target])
#         cnt = 0

#         while queue: 
#             num = queue.popleft()
#             if num == 0:
#                cnt += 1
#                continue

#             for n in nums:
#                 next_num = num - n
#                 if next_num >= 0:
#                     queue.append(next_num)



#         return cnt



# -------------OPTIMAL SOLUTION---------------
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        dp = [0] * (target+1)
        dp[0] = 1

        for i in range(1,target+1):
            for num in nums:
                if i>=num:
                    dp[i] += dp[i-num]
        
        return dp[target]


solution = Solution()
print(solution.combinationSum4([1,2,3],3)) 

