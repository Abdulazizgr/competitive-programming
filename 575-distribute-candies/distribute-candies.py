class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
      
        un = set(candyType)
    
        return min(len(un), len(candyType)//2)