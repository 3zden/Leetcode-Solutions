class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        left = 0
        right = len(s) - 1
        while right > left :
            if s[left] == s[right]:
                left, right = left + 1, right -1
            else :return False
        return True