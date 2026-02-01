class Solution(object):
    def closestNumbers(nums):
    # Write your code here
        nums.sort()
        m = float('inf')
        out = []
        for i,num in enumerate(nums[1:]):
            m = min(abs(num-nums[i]), m)

        for j in range(1,len(nums)):
            if abs(nums[j-1]-nums[j]) == m:
                out.append(nums[j-1])
                out.append(nums[j])
        return out
