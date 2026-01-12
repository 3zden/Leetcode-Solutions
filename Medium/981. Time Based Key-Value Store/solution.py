class TimeMap(object):

    def __init__(self):
        self.timeMap = []
        self.mapp = {}
        self.len = 0
        
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.mapp:
            self.timeMap.append([[key,value,timestamp]])
            self.mapp[key] = self.len
            self.len += 1
        else : self.timeMap[self.mapp[key]] += [[key,value,timestamp]]


        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        # print(self.timeMap)
        if key not in self.mapp:
            return ""
        ls = self.mapp[key]
        if len(self.timeMap[ls]) == 1 and self.timeMap[ls][0][1] <= timestamp:
            return self.timeMap[ls][0][1]
        elif self.timeMap[ls][-1][-1] < timestamp:
            return self.timeMap[ls][-1][1]
        elif self.timeMap[ls][0][-1] > timestamp:
            return ""
        l, r = 0, len(self.timeMap[ls])-1
        clos = float("inf")
        while r >= l :
            i = (r+l) // 2
            if self.timeMap[ls][i][-1] == timestamp:
                return self.timeMap[ls][i][1]
            elif self.timeMap[ls][i][-1] < timestamp:
                if (timestamp - self.timeMap[ls][i][-1]) < clos:
                    clos = self.timeMap[ls][i][1]
                l = i + 1
            else : r = i - 1
             
            # print(self.timeMap[ls],i)
        return clos


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)