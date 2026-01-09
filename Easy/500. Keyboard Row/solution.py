class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        frow = set([x for x in "qwertyuiop"])
        srow = set([x for x in "asdfghjkl"])
        trow = set([x for x in "zxcvbnm"])
        out = []
        for word in words :
            curr = set([x.lower() for x in word])
            if curr & frow == curr or curr & srow == curr or curr & trow == curr:
                out.append(word)
            else : continue
        return out