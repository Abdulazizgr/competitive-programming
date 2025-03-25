class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(mid):
            day_counter = 1
            capacity = 0
            for weight in weights:
                if capacity + weight > mid:
                    day_counter += 1
                    capacity = 0

                capacity += weight

                if day_counter > days:
                    return False

            return True
        low = max(weights)
        high = sum(weights)
        ans = high 

        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                high = mid -1
            else:
                low = mid + 1
    
        return ans 