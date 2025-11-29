class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        right = len(s) -1
        left = 0
        while right > left :
            s[right], s[left] = s[left], s[right]
            right, left = right-1, left+1
        return s       