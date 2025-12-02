class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic = {}
        for x in magazine:
            if x not in dic :
                dic[x] = 1
            else : dic[x] += 1
        for y in ransomNote :
            if y in dic:
                if dic[y] > 1 :
                    dic[y] -= 1
                else  :
                    dic.pop(y)
            else : return False 
        return True
        