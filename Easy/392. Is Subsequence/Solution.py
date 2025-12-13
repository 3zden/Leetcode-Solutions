class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i,j = 0,0
        count = len(s)
        while i < len(s) and j < len(t):
            if s[i] == t[j] :
                count -= 1
                i += 1
            j += 1
        return count == 0
        