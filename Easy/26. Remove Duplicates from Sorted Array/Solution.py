class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = set()
        i = 0
        count = 0
        while i < len(nums) :
            if nums[i] in dic and nums[i] != "x":
                nums.pop(i)
                nums.append("x")
                count += 1
            else : 
                dic.add(nums[i])
                i += 1
        return len(nums) - count
        