class Solution(object):
    def mySqrt(self, x):
        """
        :    type x: int
        :rtype: int
        """
        if x == 1: return 1
        l,r = 0,x
        cur = (r+l)//2
        while r > l:
            cur = (r+l)//2
            if cur*cur == x:
                return cur
            elif cur*cur > x:
                r = cur
            elif cur*cur < x :
                if (cur+1)*(cur+1) > x:
                    return cur
                l = cur
        return cur
