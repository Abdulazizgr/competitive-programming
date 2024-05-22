class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        one = [1] * numOnes
        an = []
        zero = [0] * numZeros
        neg = [-1] * numNegOnes
        an.extend(zero)
        an.extend(one)
        
        an.extend(neg)
        sum = 0
        an.sort(reverse=True)
        for i in range(k):
            sum += an[i]
        
        return sum