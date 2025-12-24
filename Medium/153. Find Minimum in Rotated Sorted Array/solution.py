class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        poi = len(nums) // 2
        l, r = 0 , len(nums) -1
        if len(nums) == 1: return nums[0]
        while r > l:
            if nums[poi - 1] > nums[poi]:
                return nums[poi]
            elif nums[poi - 1] < nums[poi] :
                if nums[r] < nums[poi]:
                    l = poi
                    poi += max(1,(r - l)//2)
                else :
                    r = poi
                    poi -= max(1,(r-l) // 2)