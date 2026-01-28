from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        frq = Counter(s)
        srt = sorted(frq.items(), key=lambda item:item[1])
        out = ""
        for i in range(len(srt)-1,-1,-1):
            out += srt[i][0]*srt[i][1]
        return out