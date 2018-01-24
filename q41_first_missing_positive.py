class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        arr = sorted(filter(lambda x: x > 0, nums))
        if arr:
            i = 0
            while i < len(arr):
                if (i + 1) != arr[i]:
                    return i + 1
                i += 1
            return arr[-1] + 1
        return 1
