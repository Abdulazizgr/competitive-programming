class Solution:
    def balancedStringSplit(self, s: str) -> int:
        countR = 0
        countL = 0
        ans = 0

        for val in s:
            if val == 'R':
                countR += 1
            else:
                countL += 1
            if countR == countL:
                ans += 1
                countR = 0
                countL = 0
        return ans

