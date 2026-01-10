class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        se = set([x for x in jewels])
        out = 0
        for char in stones:
            if char in se :
                out += 1
            else : continue
        return out