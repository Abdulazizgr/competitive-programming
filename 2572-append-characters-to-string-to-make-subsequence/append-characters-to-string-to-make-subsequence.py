class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n = len(t)
        f = 0
        se = 0

        while f < len(s) and se < len(t):
            if s[f] == t[se]:
                n -= 1
                f += 1
                se += 1
            else:
                f += 1
        return n 

        