# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        l, r = 1, n
        poi = max(1,n // 2)
        while poi >= 1 and poi <= n:
            if isBadVersion(poi) == True :
                if poi - 1 == 0 or isBadVersion(poi-1) == False :
                    return poi
                else :
                    r = poi
                    poi -= max(1,(r-l)//2)
            else :
                l = poi
                poi += max(1,(r-l)//2)
    
solu = Solution()
print(solu.firstBadVersion(2126753390,1702766719))