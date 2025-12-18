class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicto = {}
        for i in s:
            if i in dicto:
                dicto[i] += 1
            else: dicto[i] = 1
        pal = 0
        for v in dicto.values():
            if v % 2== 0:
                pal += v
            else : pal += v-1
        if len(s) == pal :
            return pal
        else :return pal + 1 
