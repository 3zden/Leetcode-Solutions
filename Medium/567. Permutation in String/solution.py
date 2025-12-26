class Solution(object):
    def checkInclusion(self, s1, s2):
        di = {}
        for i in s1:
            if i not in di:
                di[i] = 1
            else : di[i] += 1
        l,r = 0,len(s1)-1
        while r < len(s2):
            oi = {}
            for i in s2[l:r+1]:
                if i not in oi:
                    oi[i] = 1
                else : oi[i] += 1
            if oi == di:
                return True
            else : l,r = l+1,r+1
        return False