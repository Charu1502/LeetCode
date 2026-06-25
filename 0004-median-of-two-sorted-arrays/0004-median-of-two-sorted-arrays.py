class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_arr = nums1+nums2
        merged_arr.sort()
        ln = len(merged_arr)
        if ln%2==0:
            sum = merged_arr[ln//2-1]+merged_arr[ln//2]
            return sum/2.0
        else:
            return merged_arr[ln//2]