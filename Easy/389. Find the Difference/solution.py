from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        co = Counter(s)
        cot = Counter(t)
        return (cot - (co & cot)).keys()[-1]
        
        