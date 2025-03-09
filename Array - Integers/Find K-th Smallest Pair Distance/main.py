import heapq
class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        min_heap = []

        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                heapq.heappush(min_heap, (abs(nums[i]-nums[j])))
        
        return min_heap[k-1]

solution = Solution()
# print(solution.smallestDistancePair([1,3,1], 1))
# print(solution.smallestDistancePair([1,1,1], 2))
# print(solution.smallestDistancePair([1,6,1], 3))
print(solution.smallestDistancePair([9,10,7,10,6,1,5,4,9,8], 18))