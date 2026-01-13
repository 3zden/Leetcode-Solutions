class Solution:
    def productExceptSelf(self, nums):
        left = [1]*len(nums)
        right = [1]*len(nums)
        l, r = 1, len(nums)-2
        while  l < len(nums) and r > -1:
            left[l] = left[l-1]*nums[l-1]
            right[r] = right[r+1]*nums[r+1]
            r -= 1
            l += 1
        paes = [0]*len(nums)
        for i in range(len(nums)):
            paes[i] = left[i]*right[i]
        return paes
        