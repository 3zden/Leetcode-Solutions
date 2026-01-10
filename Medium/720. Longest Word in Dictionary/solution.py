class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        s = set(words)
        r = 1
        words.sort(reverse = True)
        out = []
        ma = 0
        for word in words: 
            if ma > len(word):
                continue
            elif len(word) == 1 and ma ==0:
                out.append(word)
            while r < len(word) and word[:r] in s:
                r += 1
                if r == len(word):
                    out.append(word)
                    ma = max(ma,len(word))
            r = 1
        if len(out) == 1:
            return out[0]
        elif len(out) == 0:
            return  ""
        else : return sorted(out)[0]