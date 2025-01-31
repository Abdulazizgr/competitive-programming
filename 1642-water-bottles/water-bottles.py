class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        n = numBottles
        ans = n
        b = numBottles
        while n >= numExchange:
            n = n // numExchange
            ans  += n
            if b % numExchange != 0:
                n += (b-numExchange*n)
            b = n

             
        
        return ans

