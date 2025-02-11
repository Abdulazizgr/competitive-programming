class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_index = 0
        citations.sort(reverse =True)
        for index,value in enumerate(citations):
            if value >= index + 1:
                h_index = index + 1
            else:
                break
        return h_index
                