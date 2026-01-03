# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        i = n//2
        l, r =0, n+1
        while r > l:
            if guess(i) == 0 :
                return i
            elif guess(i) == -1 :
                r = i
            elif guess(i) == 1 : 
                l = i
            i = (r+l)//2  