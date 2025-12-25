class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = 1
        curr = nums[0]
        mx = 0
        while r < len(nums):
            if nums[r-1]<nums[r]:
                curr +=nums[r]
                
            else :
                mx = max(curr,mx)
                curr = nums[r]
            r += 1
        mx = max(curr,mx)
        return mx
                