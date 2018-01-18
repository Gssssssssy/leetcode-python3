class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indexes = {}
        for i, num in enumerate(nums):
            indexes[num] = i
                
        for i, num_x in enumerate(nums):
            num_y = target - num_x
            if (num_y in indexes) and (indexes[num_y] != i):
                    return [i, indexes[num_y]]
            
