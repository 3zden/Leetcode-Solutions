class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        smpr = len(prices)
        streak = 0
        point = 0
        for i in range(len(prices)-1):
            if prices[i] == prices[i + 1] +1:
                point += 1
                streak += point
            else : 
                if streak == 0:
                    continue
                else : 
                    smpr += streak
                    streak = 0
                    point = 0
        smpr += streak  
        return smpr