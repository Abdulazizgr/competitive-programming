class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for i in range(len(words)):
            a = set(words[i])
            if x in a:
                ans.append(i)
        return ans
