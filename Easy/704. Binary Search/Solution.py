class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while right >= left :
            poi =  (right + left) // 2
            print(poi)
            if nums[poi] == target:
                return poi
            elif nums[poi] > target:
                right = poi -1
            else : 
                left = poi + 1 
        return -1
        