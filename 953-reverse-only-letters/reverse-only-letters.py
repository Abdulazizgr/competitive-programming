class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        ans = list(s)
        while left < right:
            temp = ans[left]
            if ans[left].isalpha():
                if ans[right].isalpha():
                    ans[left] = s[right]
                    ans[right] = temp
                    left += 1
                    right -= 1
                else:
                    right -= 1
            else:
                left += 1
        s = "".join(ans)
        return s

        