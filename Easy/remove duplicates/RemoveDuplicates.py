class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1] :
                nums.pop(i)
                nums.append(0)
                print(nums)
                print(i)
            else : i, count= i+1, count+1

        return count
    
