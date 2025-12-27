class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        pr = [0]*len(nums)
        pr[0] = nums[0]
        for i in range(1,len(nums)):
            pr[i] = pr[i-1]+nums[i]
        self.nn = pr


    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0: return self.nn[right]
        else : return self.nn[right] - self.nn[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)