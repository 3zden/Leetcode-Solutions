class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0]*n
        for i, v in enumerate(nums):
            result[i] = nums[(i+v)%n]
        return result


