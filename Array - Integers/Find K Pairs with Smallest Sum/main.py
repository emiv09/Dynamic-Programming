import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []
        
        res = []
        min_heap = []

        for i in range(min(k,len(nums1))):
            heapq.heappush(min_heap,(nums1[i] + nums2[0], i, 0))
        
        while len(res) < k and min_heap:
            summ, i, j = heapq.heappop(min_heap)
            res.append([nums1[i],nums2[j]])

            if j+1 < len(nums2):
                heapq.heappush(min_heap,(nums1[i] + nums2[j+1], i, j+1))
            
        
        return res


solution = Solution()
print(solution.kSmallestPairs([1,7,11],[2,4,6],3))