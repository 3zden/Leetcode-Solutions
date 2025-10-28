
def carFleet(target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        # duration = position / speed 
        duration = [po / sp for po in position for sp in speed ]
        return duration