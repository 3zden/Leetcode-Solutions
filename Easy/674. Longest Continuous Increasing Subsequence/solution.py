class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, 1
        ls = 0
        while r < len(nums):
            if nums[r-1] >= nums[r]:
                ls = max(ls,r-l)
                l = r
            r += 1     
        ls = max(ls,r-l)
        return ls
