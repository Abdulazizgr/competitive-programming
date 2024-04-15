class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = []
        x = str(x)
        for i in x:
            y.append(i)
        z = y[::-1]
        if y == z:
            return True
        else:
           return False