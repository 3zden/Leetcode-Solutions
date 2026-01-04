class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        poast = []
        surv = []
        for ast in asteroids:
            if ast > 0:
                poast.append(ast)
                surv.append(ast)
            else :
                while len(poast) > 0 and poast[-1] < abs(ast):
                    surv.pop(-1)
                    poast.pop(-1)
                if len(poast) > 0 and poast[-1] == abs(ast):
                    poast.pop(-1)
                    surv.pop(-1)
                elif surv == [] or surv[-1] < 0:
                    surv.append(ast)
        return surv
        