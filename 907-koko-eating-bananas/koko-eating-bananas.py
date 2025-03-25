class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isValid(mid):
            hour_counter = 0
            for pile in piles:
                hour_counter += ceil(pile/mid)
                if hour_counter > h:
                    return False
            return True
            
        low = 1
        high = max(piles)
        ans = high 

        while low <= high:
            mid = (low + high) // 2
            if isValid(mid):
                ans = mid
                high = mid -1
            else:
                low = mid + 1
    
        return ans 