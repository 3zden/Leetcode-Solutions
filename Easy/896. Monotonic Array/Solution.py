class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        state = ['pass']
        l, r = 0, 1
        while r < len(nums):  
            if nums[l] > nums[r]:
                if state[-1] == "inc":
                    return False
                state.append('dec')
            elif nums[l] < nums[r]:
                if state[-1] == "dec":
                    return False
                state.append('inc')
            l += 1
            r += 1
        return True