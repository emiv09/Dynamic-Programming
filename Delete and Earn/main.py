class Solution(object):
    def deleteAndEarn(self, nums):
        fr=[0] * 10

        for i in range(0,len(nums)):
            fr[nums[i]] += 1
        
        total_points=0

        print(fr)

        prev1=0
        prev2=0

        for i in range(0,len(fr)):
            new_points = max(prev1, prev2+i*fr[i])
            prev2=prev1
            prev1=new_points
            
        
        return prev1


solution = Solution()
print(solution.deleteAndEarn([8,3,4,7,6,6,9,2,5,8,2,4,9,5,9,1,5,7,1,4]))



        