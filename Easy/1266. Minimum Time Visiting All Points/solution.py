class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        count = 0
        p = 1
        while p < len(points):
            count += max(abs(points[p][1]-points[p-1][1]),abs(points[p][0]-points[p-1][0]))
            p += 1
        return count
                