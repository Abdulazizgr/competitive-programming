class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:    
        an = set()
        for i, j in ranges:
            for num in range(i, j + 1):
                an.add(num)
        for k in range(left, right + 1):
            if k not in an:
                return False
        return True
        