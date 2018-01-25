class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        arr = nums1 + nums2
        arr = sorted(arr)
        mid_ix = int(len(arr) / 2)
        if not (len(arr) % 2):
            return (arr[mid_ix-1] + arr[mid_ix]) / 2
        else:
            return arr[mid_ix]
