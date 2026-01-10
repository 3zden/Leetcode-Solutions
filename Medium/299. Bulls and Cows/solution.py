class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        
        di = {}
        for i, v in enumerate(secret):
            if v == guess[i]:
                continue
            if v not in di:
                di[v] = 1
            else : di[v] += 1
        bulls, cows = 0, 0
        i = 0 
        while i < len(secret):
            if secret[i]==guess[i]:
                bulls += 1
            else :
                if guess[i] in di :
                    cows += 1
                    if di[guess[i]] > 1:
                        di[guess[i]] -= 1
                    else : di.pop(guess[i])
            i += 1
        return str(bulls)+"A"+str(cows)+"B"
                     
        