class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currmax = nums[0]
        glbmax = nums[0]
        for n in nums[1:]:
            currmax = max(n, n + currmax)
            glbmax = max(currmax, glbmax)
        return glbmax
        
