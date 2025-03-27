class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def isValid(mid):
            counter = 0
            for rank in ranks:
                counter += int(sqrt(mid//rank))
            return counter >= cars
            
        low = 1
        high = max(ranks) * cars * cars
        ans = high 

        while low <= high:
            mid = (low + high) // 2
            if isValid(mid):
                ans = mid
                high = mid -1
            else:
                low = mid + 1
    
        return ans