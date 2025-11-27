class Solution(object):
    def isAnagram(self, s, t):
        # Fast length check
        if len(s) != len(t):
            return False

        counts = {}

        # Count characters in s
        for ch in s:
            if ch not in counts:
                counts[ch] = 1
            else:
                counts[ch] += 1

        # Decrease counts using t
        for ch in t:
            if ch in counts:
                if counts[ch] == 1:
                    counts.pop(ch)
                else:
                    counts[ch] -= 1
            else:
                return False

        return len(counts) == 0
