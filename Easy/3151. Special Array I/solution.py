class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i, v in enumerate(nums[1:]):
            if (v + nums[i]) % 2 == 0:
                return False
        return True