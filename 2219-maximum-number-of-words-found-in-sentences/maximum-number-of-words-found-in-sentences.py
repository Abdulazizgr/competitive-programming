class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count=0
        for sentence in sentences:
            word=len(sentence.split())
            count = max(word,count)
        return count