class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        an = []
        for i in range(len(s)):
            if s[i].isalnum():
                an.append(s[i])

        return an == an[::-1]