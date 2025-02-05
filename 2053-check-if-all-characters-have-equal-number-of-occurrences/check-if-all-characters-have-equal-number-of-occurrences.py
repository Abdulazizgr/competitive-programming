class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = Counter(s)
        n  = freq[s[0]]

        for values in freq.values():
            if n != values:
                return False
        return True
        