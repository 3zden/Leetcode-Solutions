class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0 
        c = len(nums)
        while i < c :
            if nums[i] == 0 :
                nums.append(nums.pop(i))
                c -= 1
            else : i +=1
        return nums 
        