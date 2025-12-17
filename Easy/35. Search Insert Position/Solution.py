class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        if len(nums) == 1:
            if nums[0] >= target:
                return 0
            else : return 1
        while r >= l:
            mid = (l + r) //2
            if target <= nums[mid] and (mid == 0  or target > nums[mid-1]):
                return mid
            elif nums[mid] <= target:
                l = mid + 1
            else : r = mid - 1
        if mid == len(nums) - 1:
            return mid +1