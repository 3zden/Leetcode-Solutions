class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        right = 0
        out = 0
        seto = set()
        for i in range(len(s)) :
            while right < len(s) and s[right] not in seto :
                seto.add(s[right])
                out = max(out,right - i + 1)
                right += 1
            seto.remove(s[i])
        return out