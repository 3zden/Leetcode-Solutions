from collections import Counter
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        ctr = Counter(chars)
        out = 0
        for word in words:
            copy = ctr.copy()
            breaked = False
            for ch in word:
                if ch not in copy or copy[ch] == 0: 
                    breaked = True
                    break
                else : copy[ch] -= 1
            if not breaked : out += len(word)
        return out