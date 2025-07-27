class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        lst1 = "".join(word1)
        lst2 = "".join(word2)

        return lst1 == lst2