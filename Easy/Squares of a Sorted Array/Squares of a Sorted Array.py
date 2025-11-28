class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = 0
        r = len(nums) - 1
        #out = [x**2 for x in nums]
        result = []
        while len(result) < len(nums) :
            if abs(nums[l]) >= abs(nums[r]) :
                result.insert(0,nums[l]**2)
                l += 1
            else :
                result.insert(0,nums[r]**2)
                r -= 1
        return result