class Solution:
    def sortVowels(self, s: str) -> str:
        lst = []
        vo = set("AEIOUaeiou")

        for i in range(len(s)):
            if s[i] in vo:
                lst.append(s[i])
        lst.sort()
        j = 0
        s = list(s)
        for i in range(len(s)):
            if s[i] in vo:
                s[i] = lst[j]
                j += 1



        s = "".join(s)

        return s

        