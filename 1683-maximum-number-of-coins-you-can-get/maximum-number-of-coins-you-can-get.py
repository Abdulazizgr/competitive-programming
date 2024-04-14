class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        n = len(piles)
        count = 0
        n = (n//3 )*2
       
        for i in range(1,n,2):

            count += piles[i]
        
       
        return count