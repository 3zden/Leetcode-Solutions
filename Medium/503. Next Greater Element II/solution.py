class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        st = []
        out = [-1]*len(nums)
        for i, v in enumerate(nums+nums):
            if i >= len(nums):
                i = i -len(nums)
            while st and v > st[-1][0]:
                    out[st[-1][1]] = v
                    st.pop(-1)
            st.append([v,i]) 
        return out