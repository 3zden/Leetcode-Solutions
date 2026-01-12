class Solution(object):
    def Bsearch(self, nums,target):
        l, r = 0, len(nums)-1
        while r >= l :
            i = (r + l)//2
            if nums[i] == target:
                return i
            elif nums[i] > target :
                r = i - 1
            else : l = i + 1
        return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[-1] > nums[0] or len(nums) == 1:
            return self.Bsearch(nums, target)
        else :
            rot = True
            for i in range(len(nums)-1):
                if nums[i+1] < nums[i]:
                    ron = i
                    break
                else : continue
            if target >= nums[0]:
                return self.Bsearch(nums[:ron+1],target)
            elif target <= nums[-1]:
                if self.Bsearch(nums[ron+1:],target) == -1 : return -1
                return ron +1 + self.Bsearch(nums[ron+1:],target)
            else : return -1
        
