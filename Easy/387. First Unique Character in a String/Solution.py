class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicto = {}
        popped = set()
        for i, v in enumerate(s):
            if v in dicto:
                dicto.pop(v)
                popped.add(v)
            else :
                if v not in popped:
                    dicto[v] = i
                else : continue
        if dicto != {}:
            return min(dicto.values())
        else : return -1