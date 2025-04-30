class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1),len(word2))
        index = 0
        res = ""
        while index < n:
            res += word1[index]
            res += word2[index]
            index += 1
        res += word1[index:]
        res += word2[index:]

        return res