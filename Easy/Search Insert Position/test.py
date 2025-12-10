class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[0] >= target : return 0
        elif nums[len(nums) - 1]<target : return len(nums)
        i = len(nums)//2
        while (i != 0 and i != len(nums)) :
            if target >= nums[i]:
                i += max(1, (len(nums) - i)//2)
            elif nums[i-1] >= target :
                i -= max(1, i//2)
            else : return i
        return i

solu = Solution()

solu.searchInsert([1,3,5,6], 5)