class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        for num in nums2:
            nums1.append(num)

        nums1.sort()
        mid1 = int(len(nums1)/2)
        if len(nums1) %2 == 0:
            mid1 = int(len(nums1)/2) - 1 
            mid2 = mid1 + 1 
            return float((nums1[mid1] + nums1[mid2]) / 2)
        
        return float(nums1[mid1])


solution = Solution()
print(solution.findMedianSortedArrays([1,2],[3,4]))


        