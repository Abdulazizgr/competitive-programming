class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber > 0:
            columnNumber -= 1
            rem = columnNumber % 26
            ans = chr(rem + ord("A")) + ans
            columnNumber //= 26
        return ans
