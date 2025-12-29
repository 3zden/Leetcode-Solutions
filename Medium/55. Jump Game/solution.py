class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 1:return True
        p = 0
        r = 1
        while p < n - 1:
            if nums[p] == 0 :return False
            elif nums[p] >= (n-p-1):
                return True
            else :
                if nums[r] > nums[p] - (r-p):
                    p = r
                elif r-p >= nums[p] : return False 
                r += 1
        return False