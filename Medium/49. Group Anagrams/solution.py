
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for i in strs :
            st = "".join(sorted(i))
            # print(st)
            if st in dic :
                dic[st].append(i)
            else : dic[st] = [i]
        return dic.values()
            