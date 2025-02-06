class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        values = [i for i in range(1,n+1)]
        n = len(values)
        index = 0
        while len(values)  > 1:
            a = index + (k-1)
            index = a % n
            values.pop(index)
            n = len(values)
        return values[0]
