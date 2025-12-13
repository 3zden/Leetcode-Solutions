class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(needle)
        i = 0
        while i < len(haystack) - n + 1:
            if haystack[i:i+n] == needle:
                return i
            else : i+=1
        return -1
        