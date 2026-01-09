class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start, i = -1, 0
        tank, needed = 0, 0
        found = False
        while i < len(gas):
            gap = gas[i] - cost[i] 
            if gap >= 0 :
                if not found:
                    start = i
                    found = True
                tank += gap
            else :
                if abs(gap) > tank:
                    found = False
                    tank = 0
                else : tank += gap 
            i += 1
            needed -= gap
        if not found or needed > 0:
            return -1
        else : return start