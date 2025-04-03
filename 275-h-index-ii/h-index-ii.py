class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_index = 0
        low = 0
        high = len(citations)-1
        while low <= high:
            mid = (low+high)//2

            if citations[mid] >= len(citations)-mid:
                h_index = len(citations) - mid
                high = mid - 1
            else:
                low = mid + 1


        return h_index