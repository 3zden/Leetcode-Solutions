class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        # out = letters[0]
        asc = ord(target)
        for letter in letters:
            if ord(letter) > asc :
                return letter
        return letters[0]