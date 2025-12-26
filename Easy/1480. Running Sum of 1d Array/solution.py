class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = [nums[0]]
        for i in range(1,len(nums)):
            out.append(out[i-1] + nums[i])
        return out
